from .....base.src.ui.base.UI_scale import UIScale
from ...transradial_constants import tr_ui_consts


class UIScaleScanTR(UIScale):
    bl_idname = "VIEW3D_PT_tr_scale"
    bl_label = tr_ui_consts['workflow']['scale']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_scale_scan="tr_operators.liner_scale_scan")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'scale'
                and not context.scene.ufit_circums_highlighted
                and context.scene.ufit_device_type == 'transradial')
