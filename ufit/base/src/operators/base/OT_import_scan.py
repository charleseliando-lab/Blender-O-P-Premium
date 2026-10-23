import bpy
from bpy_extras.io_utils import ImportHelper
from .....base.src.operators.core.OT_base import OTBase
from .....base.src.operators.core.start import get_scan_from_platform, save_scan_local_workspace, \
    init_modeling_folders, import_3d_file


class OTImportScan(OTBase):
    @classmethod
    def poll(cls, context):
        # always make it possible to import a scan
        if len(context.scene.ufit_medical_device) == 8:
            return True

    def main_func(self, context):
        # get the scan
        response = get_scan_from_platform(context)

        # save scan to local workspace
        scan_filepath = save_scan_local_workspace(context, response)

        obj_filepath = init_modeling_folders(context, scan_filepath)
        import_3d_file(context, obj_filepath)


# DEPRECATED
class OTImportScanOffline(OTBase, ImportHelper):
    filename_ext = ''
    filter_glob: bpy.props.StringProperty(
        default='*.zip;*.stl;*.obj;*.ply',
        options={'HIDDEN'}
    )

    @classmethod
    def poll(cls, context):
        # always make it possible to import a scan
        return True

    def invoke(self, context, event):
        if context.scene.ufit_file_type == 'zip':
            self.filter_glob = '*.zip;'
        elif context.scene.ufit_file_type == 'stl':
            self.filter_glob = '*.stl;'
        elif context.scene.ufit_file_type == 'obj':
            self.filter_glob = '*.obj;'
        elif context.scene.ufit_file_type == 'ply':
            self.filter_glob = '*.ply;'
        else:
            self.filter_glob = '*.zip;*.stl;*.obj;*.ply'
        

        return super().invoke(context, event)

    def main_func(self, context):
        obj_filepath = init_modeling_folders(context, self.filepath)
        import_3d_file(context, obj_filepath)







