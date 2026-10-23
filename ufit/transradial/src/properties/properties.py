import bpy


#################################
# Properties
#################################
tr_scene_properties = [
    'tr_connector_type',
    'tr_amputation_side',
]


def register():
    # import connector
    bpy.types.Scene.tr_connector_type = bpy.props.EnumProperty(name="Connector Type", default=1,
                                                               items=[
                                                                   ("universal_wrist_connector_50mm.blend", "Universal Wrist 50mm", "", 1),
                                                                   ("universal_wrist_connector_with_bottom_50mm.blend", "Universal Wrist With Bottom 50mm", "", 2),
                                                                   ("new_connector.blend", "Slide in Oval", "", 3)
                                                               ])

    bpy.types.Scene.tr_amputation_side = bpy.props.EnumProperty(name="Side", default=1,
                                                                items=[
                                                                    ("right", "right", "", 1),
                                                                    ("left", "left", "", 2),
                                                                ])


def unregister():
    # import connector
    del bpy.types.Scene.tr_connector_type
    del bpy.types.Scene.tr_amputation_side

