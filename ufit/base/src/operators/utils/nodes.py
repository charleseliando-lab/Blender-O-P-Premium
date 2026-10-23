import bpy


def has_texture(obj):
    # Check if the object is valid
    if obj is None or obj.type != 'MESH':
        return False

    # Iterate through material slots
    for slot in obj.material_slots:
        material = slot.material

        # Check if the material has texture slots
        if material and material.use_nodes:
            if material.node_tree and material.node_tree.nodes:
                for node in material.node_tree.nodes:
                    if node.type == 'TEX_IMAGE':
                        return True

    return False


#######################################
# Shader Nodes
#######################################
def set_push_pull_smooth_shader_nodes(ufit_obj, color_attr_name):
    if not ufit_obj.data.materials:
        # Create a new material
        material = bpy.data.materials.new(name='texture')

        # Link the material to the ufit object
        ufit_obj.data.materials.append(material)

        # use nodes
        material.use_nodes = True

    material = ufit_obj.data.materials[ufit_obj.active_material_index]

    # remove all nodes
    material.node_tree.nodes.clear()

    # nodes - selection
    node_color_attr_one = material.node_tree.nodes.new('ShaderNodeVertexColor')
    node_color_attr_one.layer_name = 'area_selection'

    node_color_invert = material.node_tree.nodes.new('ShaderNodeInvert')

    node_separate_color = material.node_tree.nodes.new('ShaderNodeSeparateColor')
    node_separate_color.mode = 'RGB'

    # node - scan colors
    node_color_attr_two = material.node_tree.nodes.new('ShaderNodeVertexColor')
    node_color_attr_two.layer_name = 'scan_colors'

    # node - RGB
    node_rgb = material.node_tree.nodes.new('ShaderNodeRGB')
    node_rgb.outputs['Color'].default_value = (0.0, 1.0, 0.0, 1.0)  # selection in green

    # node mix to output
    node_mix = material.node_tree.nodes.new('ShaderNodeMix')
    node_mix.data_type = 'RGBA'
    node_mix.blend_type = 'MULTIPLY'
    node_mix.clamp_result = True
    node_mix.clamp_factor = False

    node_emmision = material.node_tree.nodes.new('ShaderNodeEmission')

    node_material_output = material.node_tree.nodes.new('ShaderNodeOutputMaterial')

    # Node links - color attribute selection to mix
    material.node_tree.links.new(
        node_color_attr_one.outputs['Color'],
        node_color_invert.inputs['Color']
    )
    material.node_tree.links.new(
        node_color_invert.outputs['Color'],
        node_separate_color.inputs['Color']
    )
    material.node_tree.links.new(
        node_separate_color.outputs['Red'],
        node_mix.inputs['Factor']
    )

    # Node link - scan colors to mix
    material.node_tree.links.new(
        node_color_attr_two.outputs['Color'],
        node_mix.inputs[6]
    )

    # Node link - RGB to mix
    material.node_tree.links.new(
        node_rgb.outputs['Color'],
        node_mix.inputs[7]  # multiple 'B' inputs, we need to select type RGBA which is at index 7
    )

    # Node links - Emission to Output
    material.node_tree.links.new(
        node_mix.outputs[2],  # multiple 'Result' output, we need to select type RGBA which is at index 2
        node_emmision.inputs['Color']
    )
    material.node_tree.links.new(
        node_emmision.outputs['Emission'],
        node_material_output.inputs['Surface'],
    )


#######################################
# Geometry Nodes
#######################################
def set_voronoi_geometry_nodes_one(ufit_obj, tree_name, color_attr_name):
    # Check if the node tree already exists
    if tree_name not in bpy.data.node_groups:
        # Create a new geometry nodes modifer (automatically creates a node_group with name "Geometry Nodes"
        bpy.ops.node.new_geometry_nodes_modifier()

        # Rename the new node tree
        bpy.data.node_groups[0].name = tree_name

        # Access the geometry nodes tree
        node_tree = bpy.data.node_groups[tree_name]

        in_node = node_tree.nodes["Group Input"]
        out_node = node_tree.nodes["Group Output"]

        named_attribute = node_tree.nodes.new(type="GeometryNodeInputNamedAttribute")
        named_attribute.data_type = 'FLOAT_COLOR'
        named_attribute.inputs[0].default_value = color_attr_name

        equal_node = node_tree.nodes.new(type="FunctionNodeCompare")
        equal_node.data_type = 'RGBA'
        equal_node.operation = 'EQUAL'
        equal_node.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0)
        equal_node.inputs[12].default_value = 0.1

        voronoi_node = node_tree.nodes.new(type="ShaderNodeTexVoronoi")
        voronoi_node.name = 'ufit_voronoi_node'  # provide name so we can access it for UI
        voronoi_node.voronoi_dimensions = '3D'
        voronoi_node.feature = 'DISTANCE_TO_EDGE'
        voronoi_node.inputs[2].default_value = 15.0  # scale
        voronoi_node.inputs[5].default_value = 1  # random

        greater_than_node = node_tree.nodes.new(type="FunctionNodeCompare")
        greater_than_node.name = 'ufit_compare_node'  # provide name so we can access it for UI
        greater_than_node.data_type = 'FLOAT'
        greater_than_node.operation = 'GREATER_THAN'
        greater_than_node.inputs[1].default_value = 0.2

        boolean_and_node = node_tree.nodes.new(type="FunctionNodeBooleanMath")
        boolean_and_node.operation = 'AND'

        delete_geometry_node = node_tree.nodes.new(type="GeometryNodeDeleteGeometry")
        delete_geometry_node.domain = 'POINT'
        delete_geometry_node.mode = 'ALL'

        edge_neighbours = node_tree.nodes.new(type="GeometryNodeInputMeshEdgeNeighbors")

        equal_node_two = node_tree.nodes.new(type="FunctionNodeCompare")
        equal_node_two.data_type = 'INT'
        equal_node_two.operation = 'EQUAL'
        equal_node_two.inputs[3].default_value = 1

        evaluate_on_domain = node_tree.nodes.new(type="GeometryNodeFieldOnDomain")
        evaluate_on_domain.data_type = 'BOOLEAN'
        evaluate_on_domain.domain = 'EDGE'

        not_node = node_tree.nodes.new(type="FunctionNodeBooleanMath")
        not_node.operation = 'NOT'

        delete_geometry_node_two = node_tree.nodes.new(type="GeometryNodeDeleteGeometry")
        delete_geometry_node_two.domain = 'EDGE'
        delete_geometry_node_two.mode = 'ALL'

        mesh_to_curve = node_tree.nodes.new(type="GeometryNodeMeshToCurve")

        set_position_node = node_tree.nodes.new(type="GeometryNodeSetPosition")

        position_node = node_tree.nodes.new(type="GeometryNodeInputPosition")

        blur_attribute = node_tree.nodes.new(type="GeometryNodeBlurAttribute")
        blur_attribute.data_type = 'FLOAT_VECTOR'
        blur_attribute.inputs[4].default_value = 10  # iterations
        blur_attribute.inputs[5].default_value = 1  # weight

        curve_to_mesh = node_tree.nodes.new(type="GeometryNodeCurveToMesh")

        sample_nearest = node_tree.nodes.new(type="GeometryNodeSampleNearest")
        sample_nearest.domain = 'POINT'

        sample_index = node_tree.nodes.new(type="GeometryNodeSampleIndex")
        sample_index.data_type = 'FLOAT_VECTOR'
        sample_index.domain = 'POINT'

        position_node_two = node_tree.nodes.new(type="GeometryNodeInputPosition")

        edge_neighbours_two = node_tree.nodes.new(type="GeometryNodeInputMeshEdgeNeighbors")

        equal_node_three = node_tree.nodes.new(type="FunctionNodeCompare")
        equal_node_three.data_type = 'INT'
        equal_node_three.operation = 'EQUAL'
        equal_node_three.inputs[3].default_value = 1

        evaluate_on_domain_two = node_tree.nodes.new(type="GeometryNodeFieldOnDomain")
        evaluate_on_domain_two.data_type = 'BOOLEAN'
        evaluate_on_domain_two.domain = 'EDGE'

        set_position_node_two = node_tree.nodes.new(type="GeometryNodeSetPosition")

        join_geometry_node = node_tree.nodes.new(type="GeometryNodeJoinGeometry")

        named_attribute_two = node_tree.nodes.new(type="GeometryNodeInputNamedAttribute")
        named_attribute_two.data_type = 'FLOAT_COLOR'
        named_attribute_two.inputs[0].default_value = color_attr_name

        not_equal_node = node_tree.nodes.new(type="FunctionNodeCompare")
        not_equal_node.data_type = 'RGBA'
        not_equal_node.operation = 'NOT_EQUAL'
        not_equal_node.inputs[7].default_value = (1.0, 1.0, 0.0, 1.0)
        not_equal_node.inputs[12].default_value = 0.1

        set_position_node_three = node_tree.nodes.new(type="GeometryNodeSetPosition")

        extrude_mesh_node = node_tree.nodes.new(type="GeometryNodeExtrudeMesh")
        extrude_mesh_node.name = 'ufit_extrude_node'
        extrude_mesh_node.inputs[3].default_value = bpy.context.scene.ufit_voronoi_one_thickness/1000
        extrude_mesh_node.inputs[4].default_value = False  # individual

        flip_faces_node = node_tree.nodes.new(type="GeometryNodeFlipFaces")

        join_geometry_node_two = node_tree.nodes.new(type="GeometryNodeJoinGeometry")

        merge_by_dist_node = node_tree.nodes.new(type="GeometryNodeMergeByDistance")
        merge_by_dist_node.inputs[2].default_value = 0.0001  # 0.01cm

        set_position_node_four = node_tree.nodes.new(type="GeometryNodeSetPosition")

        ####################
        # node links
        ####################
        node_tree.links.new(named_attribute.outputs[2], equal_node.inputs[6])
        node_tree.links.new(equal_node.outputs['Result'], boolean_and_node.inputs[1])
        node_tree.links.new(voronoi_node.outputs['Distance'], greater_than_node.inputs[0])
        node_tree.links.new(greater_than_node.outputs['Result'], boolean_and_node.inputs[0])

        node_tree.links.new(in_node.outputs['Geometry'], delete_geometry_node.inputs['Geometry'])
        node_tree.links.new(boolean_and_node.outputs['Boolean'], delete_geometry_node.inputs['Selection'])

        node_tree.links.new(edge_neighbours.outputs[0], equal_node_two.inputs[2])
        node_tree.links.new(equal_node_two.outputs['Result'], evaluate_on_domain.inputs[4])
        node_tree.links.new(evaluate_on_domain.outputs[4], not_node.inputs['Boolean'])
        node_tree.links.new(not_node.outputs['Boolean'], delete_geometry_node_two.inputs['Selection'])

        node_tree.links.new(delete_geometry_node.outputs['Geometry'], delete_geometry_node_two.inputs['Geometry'])
        node_tree.links.new(delete_geometry_node_two.outputs['Geometry'], mesh_to_curve.inputs['Mesh'])
        node_tree.links.new(mesh_to_curve.outputs['Curve'], set_position_node.inputs['Geometry'])

        node_tree.links.new(position_node.outputs['Position'], blur_attribute.inputs[2])
        node_tree.links.new(blur_attribute.outputs[2], set_position_node.inputs['Position'])

        node_tree.links.new(set_position_node.outputs['Geometry'], curve_to_mesh.inputs['Curve'])

        node_tree.links.new(curve_to_mesh.outputs['Mesh'], sample_nearest.inputs['Geometry'])
        node_tree.links.new(position_node_two.outputs['Position'], sample_index.inputs[3])
        node_tree.links.new(sample_nearest.outputs['Index'], sample_index.inputs['Index'])
        node_tree.links.new(curve_to_mesh.outputs['Mesh'], sample_index.inputs['Geometry'])

        node_tree.links.new(edge_neighbours_two.outputs[0], equal_node_three.inputs[2])
        node_tree.links.new(equal_node_three.outputs['Result'], evaluate_on_domain_two.inputs[4])
        node_tree.links.new(evaluate_on_domain_two.outputs[4], set_position_node_two.inputs['Selection'])
        node_tree.links.new(delete_geometry_node.outputs['Geometry'], set_position_node_two.inputs['Geometry'])
        node_tree.links.new(sample_index.outputs[2], set_position_node_two.inputs['Position'])

        node_tree.links.new(set_position_node_two.outputs['Geometry'], join_geometry_node.inputs['Geometry'])
        node_tree.links.new(curve_to_mesh.outputs['Mesh'], join_geometry_node.inputs['Geometry'])

        node_tree.links.new(named_attribute_two.outputs[2], not_equal_node.inputs[6])
        node_tree.links.new(not_equal_node.outputs['Result'], set_position_node_three.inputs['Selection'])
        node_tree.links.new(join_geometry_node.outputs['Geometry'], set_position_node_three.inputs['Geometry'])

        node_tree.links.new(set_position_node_three.outputs['Geometry'], extrude_mesh_node.inputs['Mesh'])
        node_tree.links.new(set_position_node_three.outputs['Geometry'], flip_faces_node.inputs['Mesh'])

        node_tree.links.new(extrude_mesh_node.outputs['Mesh'], join_geometry_node_two.inputs['Geometry'])
        node_tree.links.new(flip_faces_node.outputs['Mesh'], join_geometry_node_two.inputs['Geometry'])

        node_tree.links.new(join_geometry_node_two.outputs['Geometry'], merge_by_dist_node.inputs['Geometry'])

        node_tree.links.new(not_equal_node.outputs['Result'], set_position_node_four.inputs['Selection'])
        node_tree.links.new(merge_by_dist_node.outputs['Geometry'], set_position_node_four.inputs['Geometry'])

        node_tree.links.new(set_position_node_four.outputs['Geometry'], out_node.inputs['Geometry'])

    else:
        geometry_modifier = ufit_obj.modifiers.new(name="Geometry Nodes", type='NODES')
        geometry_modifier.node_group = bpy.data.node_groups[tree_name]


def set_voronoi_geometry_nodes_two(ufit_obj, tree_name, color_attr_name):
    # Check if node tree already exists
    if tree_name not in bpy.data.node_groups:
        # Create a new geometry nodes modifer (automatically creates a node_group with name "Geometry Nodes"
        bpy.ops.node.new_geometry_nodes_modifier()

        # Rename the new node tree to "Voronoi Nodes Two"
        bpy.data.node_groups[0].name = tree_name

        # Access the "Voronoi Nodes Two" geometry nodes tree
        node_tree = bpy.data.node_groups[tree_name]

        in_node = node_tree.nodes["Group Input"]
        out_node = node_tree.nodes["Group Output"]

        named_attribute = node_tree.nodes.new(type="GeometryNodeInputNamedAttribute")
        named_attribute.data_type = 'FLOAT_COLOR'
        named_attribute.inputs[0].default_value = color_attr_name

        equal_node = node_tree.nodes.new(type="FunctionNodeCompare")
        equal_node.data_type = 'RGBA'
        equal_node.operation = 'EQUAL'
        equal_node.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0)
        equal_node.inputs[12].default_value = 0.1

        dual_mesh_node = node_tree.nodes.new(type="GeometryNodeDualMesh")
        dual_mesh_node.inputs[1].default_value = True  # keep boundaries

        extrude_mesh_node_one = node_tree.nodes.new(type="GeometryNodeExtrudeMesh")
        extrude_mesh_node_one.mode = 'FACES'
        extrude_mesh_node_one.inputs[3].default_value = 0

        scale_elements_node = node_tree.nodes.new(type="GeometryNodeScaleElements")
        scale_elements_node.inputs[2].default_value = 0.7

        # scale_elements_node = node_tree.nodes.new(type="GeometryNodeScaleElements")

        delete_geometry_node = node_tree.nodes.new(type="GeometryNodeDeleteGeometry")
        delete_geometry_node.domain = 'FACE'
        delete_geometry_node.mode = 'ALL'

        extrude_mesh_node_two = node_tree.nodes.new(type="GeometryNodeExtrudeMesh")
        extrude_mesh_node_two.name = 'ufit_extrude_node'
        extrude_mesh_node_two.inputs[3].default_value = bpy.context.scene.ufit_voronoi_two_thickness/1000  # thickness
        extrude_mesh_node_two.inputs[4].default_value = False  # individual

        flip_faces_node = node_tree.nodes.new(type="GeometryNodeFlipFaces")

        join_geometry_node = node_tree.nodes.new(type="GeometryNodeJoinGeometry")

        merge_by_dist_node = node_tree.nodes.new(type="GeometryNodeMergeByDistance")
        merge_by_dist_node.inputs[2].default_value = 0.0001

        subdivision_surface_node = node_tree.nodes.new(type="GeometryNodeSubdivisionSurface")
        subdivision_surface_node.inputs[1].default_value = 1

        shade_smooth_node = node_tree.nodes.new(type="GeometryNodeSetShadeSmooth")

        node_tree.links.new(in_node.outputs['Geometry'], dual_mesh_node.inputs['Mesh'])
        node_tree.links.new(named_attribute.outputs[2], equal_node.inputs[6])
        node_tree.links.new(equal_node.outputs['Result'], extrude_mesh_node_one.inputs['Selection'])
        node_tree.links.new(dual_mesh_node.outputs['Dual Mesh'], extrude_mesh_node_one.inputs['Mesh'])
        node_tree.links.new(extrude_mesh_node_one.outputs['Mesh'], scale_elements_node.inputs['Geometry'])
        node_tree.links.new(extrude_mesh_node_one.outputs['Top'], scale_elements_node.inputs['Selection'])
        node_tree.links.new(extrude_mesh_node_one.outputs['Top'], delete_geometry_node.inputs['Selection'])
        node_tree.links.new(scale_elements_node.outputs['Geometry'], delete_geometry_node.inputs['Geometry'])
        node_tree.links.new(delete_geometry_node.outputs['Geometry'], extrude_mesh_node_two.inputs['Mesh'])
        node_tree.links.new(delete_geometry_node.outputs['Geometry'], flip_faces_node.inputs['Mesh'])
        node_tree.links.new(extrude_mesh_node_two.outputs['Mesh'], join_geometry_node.inputs['Geometry'])
        node_tree.links.new(flip_faces_node.outputs['Mesh'], join_geometry_node.inputs['Geometry'])
        node_tree.links.new(join_geometry_node.outputs['Geometry'], merge_by_dist_node.inputs['Geometry'])
        node_tree.links.new(merge_by_dist_node.outputs['Geometry'], subdivision_surface_node.inputs['Mesh'])
        node_tree.links.new(subdivision_surface_node.outputs['Mesh'], shade_smooth_node.inputs['Geometry'])
        node_tree.links.new(shade_smooth_node.outputs['Geometry'], out_node.inputs['Geometry'])

    else:
        geometry_modifier = ufit_obj.modifiers.new(name="Geometry Nodes", type='NODES')
        geometry_modifier.node_group = bpy.data.node_groups[tree_name]
