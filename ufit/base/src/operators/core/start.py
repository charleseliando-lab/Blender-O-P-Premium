import os
import json
import base64
import shutil
import zipfile
from datetime import datetime
import bpy
from .checkpoints import (
    recalc_ufit_paths,
    set_active_step,
    clear_checkpoints,
    get_workflow_step,
)
from ....src import base_globals
from ..utils import general, nodes, user_interface


#################################
# Start new / Start from existing
#################################
def start_modeling(context):
    # reset progress
    context.scene.ufit_progress = 0

    # set view_3d area full window
    # bpy.ops.wm.window_new()
    context.scene.ufit_full_screen = True


def start_from_existing(context, file_path_obj, path_consts, ui_consts, debug_step=None):
    modeling_folder = os.path.dirname(file_path_obj)
    checkpoints_dir = os.path.join(modeling_folder, "checkpoints")
    file_path = os.path.join(checkpoints_dir, 'uFit_settings.txt')
    add_on_version = user_interface.get_addon_version('uFit Premium')

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if "uFit Version" in line:
                    ufit_version = line.split(":")[1].strip()
                    break
    else:
        raise Exception(f"The uFit_settings.txt file does not exist")

    if add_on_version.split('.')[0].strip() != ufit_version.split('.')[0].strip():
        raise Exception(f"The 3D model was created with uFit version {ufit_version} "
                        f"and that is not compatible with your current uFit Premium Version: {add_on_version}."
                        f"Go to our website for more information")

    if os.path.isdir(checkpoints_dir):
        device_type = context.scene.ufit_device_type
        if context.scene.ufit_device_type == 'free_sculpting':
            device_type_abbr = "FS"       
        elif context.scene.ufit_device_type == 'transfemoral':
            device_type_abbr = "TF"
        elif context.scene.ufit_device_type == 'transradial':
            device_type_abbr = "TR"
        else:
            device_type_abbr = "TT"
        
        modeling_folder_name = os.path.basename(os.path.normpath(modeling_folder))

        if not (device_type_abbr in modeling_folder_name or device_type in modeling_folder_name):
            raise Exception(f"The chosen device type does not match the folder name")

        checkpoints_files = os.listdir(checkpoints_dir)
        checkpoints_files.reverse()
        latest_checkpoint = None
        active_step = None

        workflow = list(ui_consts['workflow'].keys())
        workflow.reverse()
        for step in workflow:
            for file in checkpoints_files:
                if file.startswith('ST_'):
                    wf_step = get_workflow_step(step, path_consts)
                    if wf_step \
                            and wf_step in file \
                            and 'blend1' not in file \
                            and (not debug_step or step == debug_step):
                        latest_checkpoint = os.path.join(checkpoints_dir, file)
                        active_step = step
                        break

            # also break out of big for loop
            if latest_checkpoint and active_step:
                break

        if latest_checkpoint:
            bpy.ops.wm.open_mainfile(filepath=latest_checkpoint)
            recalc_ufit_paths(context, modeling_folder, checkpoints_dir)
            set_active_step(context, active_step, path_consts, ui_consts)

            return None

    raise Exception(f"No checkpoint folder found. Please use 'Create New' for this scan.")


#################################
# Import Scan
#################################
def get_scan_from_platform(context):
    fetch_error_one = "Could not find the Medical Device ID."
    fetch_error_two = "Could not find any 3D scans for the given Medical Device ID."

    url_get_scan = f'{context.scene.ufit_platform}/ugani/get/medical_device/3d_scans'
    data = {
        "params": {
            "medical_device_id": context.scene.ufit_medical_device
        }
    }

    for i in range(10):
        try:
            r = base_globals.platform_session.post(url=url_get_scan, data=json.dumps(data), headers=base_globals.headers)
            if r.ok and r.json():
                if not r.json()['result'].get('response'):
                    raise Exception(fetch_error_one)
                elif not r.json()['result']['response']['scans']:
                    raise Exception(fetch_error_two)

                return r.json()['result']['response']

        except Exception as e:
            if str(e) in [fetch_error_one, fetch_error_two]:
                raise Exception(str(e))  # we need to raise it again to stop the for loop from continuing

            print('Unexpected network error, trying again')

    raise Exception(f'Download failed for no clear reason. Please contact uFit support.')


def save_scan_local_workspace(context, response):
    ufit_prefs = bpy.context.preferences.addons['ufit'].preferences

    context.scene.ufit_patient_file = response['patient_file_id']
    context.scene.platform_info_complete = True

    patient_name = response['patient_name']
    medical_device = response['medical_device_id']
    scan_name = response['scans'][0]['name']
    encoded_zip = response['scans'][0]['attachment_base64']  # comes in as base64 encoded string

    patient_folder = f'{ufit_prefs.workspace}{context.scene.ufit_patient_file} - {patient_name}'
    scan_location = f'{patient_folder}/{scan_name}'

    # create patient directory if it does not exists
    if not os.path.exists(patient_folder):
        os.makedirs(patient_folder)

    # create zip file (decode b64 encodation)
    zip_file = open(scan_location, 'wb')  # make sure to write binary for zip file
    zip_file.write(base64.b64decode(encoded_zip))
    zip_file.close()

    # # extract the zip file
    # zip_extract_folder = zip_location.replace('.zip', '')
    # with zipfile.ZipFile(zip_location, 'r') as zip_ref:
    #     zip_ref.extractall(zip_extract_folder)
    #
    # # delete the zip file
    # os.remove(zip_location)

    return scan_location


def init_modeling_folders(context, filepath):
    file_name = os.path.basename(filepath)
    file_folder = os.path.dirname(filepath)

    # make sure you are not inside a modeling folder that already has checkpoints
    if not os.path.isdir(f'{file_folder}/checkpoints'):

        # define and create modeling folder
        ts = datetime.now().strftime("%y%m%d_%H%M%S")

        medical_device = context.scene.ufit_medical_device

        if context.scene.ufit_device_type == 'free_sculpting':
            device_type = "FS"       
        elif context.scene.ufit_device_type == 'transfemoral':
            device_type = "TF"
        elif context.scene.ufit_device_type == 'transradial':
            device_type = "TR"
        else:
            device_type = "TT"

        modeling_folder = f'{file_folder}/{medical_device}_{device_type}_{ts}'

        os.makedirs(modeling_folder)

        # scan file name and checkpoint folders
        context.scene.ufit_scan_filename = f'{file_name.split(".")[0]}'
        context.scene.ufit_folder_modeling = modeling_folder
        context.scene.ufit_folder_checkpoints = f'{modeling_folder}/checkpoints'

        # copy zip file to modeling folder
        # shutil.copy2(filepath, f'{modeling_folder}/{file_name}')
        obj_filepath = None

        if filepath.endswith(".obj"):

            png_file = next((os.path.join(file_folder, file) for file in os.listdir(file_folder) if file
                            .endswith(".png")), None)
            mtl_file = next((os.path.join(file_folder, file) for file in os.listdir(file_folder) if file
                            .endswith(".mtl")), None)
            if png_file and mtl_file:
                shutil.copy2(filepath, f'{modeling_folder}')
                shutil.copy2(png_file, f'{modeling_folder}')
                shutil.copy2(mtl_file, f'{modeling_folder}')
                obj_filepath = f'{modeling_folder}/{file_name}'  # not sure about the path
                context.scene.ufit_scan_filename = file_name.split(".")[0]
            else:
                raise Exception(f" MTL /PNG files are missing")
        elif filepath.endswith(".stl"):

            shutil.copy2(filepath, f'{modeling_folder}')
            obj_filepath = f'{modeling_folder}/{file_name}'
            context.scene.ufit_scan_filename = file_name.split(".")[0]

        elif filepath.endswith(".zip"):
           # extract the zip file
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(modeling_folder)

            # store checkpoints folder and scan_filename
            for file in os.listdir(modeling_folder):
                if file.endswith(".obj") or file.endswith(".stl") or file.endswith(".ply"):
                    obj_filepath = f'{modeling_folder}/{file}'
                    #testing error handling to if this works
                    try:
                        context.scene.ufit_scan_filename = file.split(".")[0]
                    except:
                        raise Exception('Could not find a valid file in the zip file')
                    break

        if not obj_filepath:
            raise Exception('Could not find an .obj, .stl or .ply file in scan folder')

        clear_checkpoints(context)
        return obj_filepath

    else:
        raise Exception(f"Found checkpoints folder. You can't use 'Create New' in this location.")

def get_active_color_attribute(obj):
    if not obj or obj.type != 'MESH':
        print("[uFit] No valid mesh object.")
        return None

    color_attributes = obj.data.color_attributes
    if not color_attributes:
        print("[uFit] No color attributes found.")
        return None

    active_attr = color_attributes.active_color
    if active_attr:
        print("[uFit] Active color attribute:", active_attr.name)
        return active_attr
    else:
        print("[uFit] No active color attribute set.")
        return None
    
def create_material(name, attribute_name):
    # Create a new material
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True

    # Clear existing nodes
    nodes = mat.node_tree.nodes
    nodes.clear()

    # Create nodes
    output_node = nodes.new(type="ShaderNodeOutputMaterial")
    bsdf_node = nodes.new(type="ShaderNodeBsdfPrincipled")
    attr_node = nodes.new(type="ShaderNodeAttribute")

    # Set attribute node's name
    attr_node.attribute_name = attribute_name

    # Position nodes
    attr_node.location = (-600, 0)
    bsdf_node.location = (-300, 0)
    output_node.location = (0, 0)

    # Link nodes
    links = mat.node_tree.links
    links.new(attr_node.outputs["Color"], bsdf_node.inputs["Base Color"])
    links.new(bsdf_node.outputs["BSDF"], output_node.inputs["Surface"])

    print(f"[uFit] Material '{name}' created with Attribute -> Principled BSDF -> Material Output")

    return mat

def import_3d_file(context, filepath):
    # delete everything from the scene
    general.delete_scene(context)
    # load the new object

    if filepath.endswith(".obj"):
        # bpy.ops.import_scene.obj(filepath=filepath)
        bpy.ops.wm.obj_import(filepath=filepath)
    elif filepath.endswith(".stl"):
        bpy.ops.import_mesh.stl(filepath=filepath)
    elif filepath.endswith(".ply"):
        bpy.ops.import_mesh.ply(filepath=filepath)
    # rename the object
    obj_scan = bpy.context.selected_objects[0]
    obj_scan.name = 'uFit'

    # check if the object has a texture
    if not nodes.has_texture(obj_scan):
        color_attr = get_active_color_attribute(obj_scan)
        if color_attr:
            context.scene.ufit_colored_attribute_scan = True
            color_attr.name = 'scan_colors'
            mat = create_material("uFit_Colored_Material", color_attr.name)
            # Clear all existing materials
            obj_scan.data.materials.clear()

            # Assign the new material
            obj_scan.data.materials.append(mat)

            print(f"Material '{mat.name}' created and assigned to '{obj_scan.name}', old materials removed.")
        else:
            context.scene.ufit_colored_scan = False
            context.scene.ufit_colored_attribute_scan = False
    else:
        context.scene.ufit_colored_scan = True
        context.scene.ufit_colored_attribute_scan = False

    # remove any rotation, location and scaling changes
    obj_scan.rotation_euler = (0, 0, 0)
    obj_scan.location = (0, 0, 0)
    obj_scan.scale = (1, 1, 1)

    # Perform scaling by user
    scale = context.scene.ufit_scan_scale_size
    obj_scan.scale = (scale, scale, scale)

    # activate object
    context.view_layer.objects.active = obj_scan

    # apply scaling
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
