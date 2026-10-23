import bpy


#################################
# Properties
#################################
tf_scene_properties = [
    'tf_connector_type',
    'tf_foot_type',
    'tf_amputation_side',
]


def register():
    # import connector
    bpy.types.Scene.tf_connector_type = bpy.props.EnumProperty(name="Connector Type", default=1,
                                                               items=[
                                                                ("universal_4_hole_quad.blend", "Universal 4-hole Quad", "", 1),
                                                                   ("universal_4_hole_circ.blend", "Universal 4-hole Circ", "", 2),
                                                                   ("universal_4_hole_circ_small.blend", "Universal 4-hole Circ (Small)", "", 3),
                                                                   ("universal_4_hole_circ_child.blend", "Universal 4-hole Circ (Child)", "", 4),
                                                                   ("spherical_circ_S-size.blend", "Spherical Circ S-size", "", 5),
                                                                   ("spherical_circ_L-size.blend", "Spherical Circ L-size", "", 6),
                                                                   ("regal_shutterlock_65mm.blend", "Universal Regal Connector 65mm", "", 7),
                                                                   ("regal_shutterlock_68mm.blend", "Universal Regal Connector 68mm", "", 8),
                                                                   ("universal_circ_regal_willowwood_alpha.blend", "Universal Willow Wood Alpha", "", 9),
                                                                   ("alps_shutterlock.blend", "Alps Shutterlock", "", 10),
                                                                   ("teh_lin_connector.blend", "Teh Lin Connector", "", 11),
                                                                   ("endo_socket_lock.blend", "Endo Socket", "", 12),
                                                                   ("spherical_circ_S-size_non_flat.blend", "Spherical Circ S-size (Supports needed)", "", 13),
                                                                   ("spherical_circ_L-size_non_flat.blend", "Spherical Circ L-size (Supports needed)", "", 14),
                                                                    ("universal_no_hole_circ.blend", "No holes", "", 15),
                                                                    ("separated_connector.blend", "Aeki Connector", "", 16),
                                                               ])

    bpy.types.Scene.tf_foot_type = bpy.props.EnumProperty(name="Foot Type", default=1,
                                                          items=[
                                                              ("basic_foot.blend", "basic", "", 1),
                                                          ])

    bpy.types.Scene.tf_amputation_side = bpy.props.EnumProperty(name="Side", default=1,
                                                                items=[
                                                                    ("right", "right", "", 1),
                                                                    ("left", "left", "", 2),
                                                                ])


def unregister():
    # import connector
    del bpy.types.Scene.tf_connector_type
    del bpy.types.Scene.tf_foot_type
    del bpy.types.Scene.tf_amputation_side

