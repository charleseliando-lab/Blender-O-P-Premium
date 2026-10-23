from .....base.src.ui.base.UI_connector import UITransitionConnector
from ...transradial_constants import tr_ui_consts
from .....base.src.ui.utils.general import get_standard_navbox


class UITransitionConnectorTR(UITransitionConnector):
    bl_idname = "VIEW3D_PT_tr_transition_connector"
    bl_label = tr_ui_consts['workflow']['transition']['ui_name']

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        active_object = context.active_object

        self.draw_base(context,
                       ot_transition_connector="tr_operators.transition_connector")
        
       
        

        
        
        

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'transition'
                and not context.scene.ufit_circums_highlighted
                and context.scene.ufit_device_type == 'transradial')
