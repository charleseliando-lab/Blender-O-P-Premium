from .....base.src.ui.base.UI_thickness import UIVerifyThickness
from ...transradial_constants import tr_ui_consts


class UIVerifySocketTR(UIVerifyThickness):
    bl_idname = "VIEW3D_PT_tr_verify_socket"
    bl_label = tr_ui_consts['workflow']['verify_socket']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_approve_thickness="tr_operators.approve_socket")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'verify_socket'
                and not context.scene.ufit_circums_highlighted
                and context.scene.ufit_device_type == 'transradial')
