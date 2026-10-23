from .....base.src.ui.base.UI_rotate import UIRotate
from ...transradial_constants import tr_ui_consts


class UIRotateTR(UIRotate):
    bl_idname = "VIEW3D_PT_tr_rotate_scan"
    bl_label = tr_ui_consts['workflow']['rotate']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_save_rotation="tr_operators.save_rotation")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'rotate'
                and context.scene.ufit_device_type == 'transradial')
