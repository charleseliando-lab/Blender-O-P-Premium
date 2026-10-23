from .....base.src.ui.base.UI_indicate import UIIndicate
from ...transradial_constants import tr_ui_consts


class UIMoveScanTR(UIIndicate):
    bl_idname = "VIEW3D_PT_tr_move_scan"
    bl_label = tr_ui_consts['workflow']['indicate']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_move_scan="tr_operators.move_scan")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'indicate'
                and context.scene.ufit_device_type == 'transradial')
