from .....base.src.ui.base.UI_thickness import UIThickness
from ...transradial_constants import tr_ui_consts


class UIThicknessTR(UIThickness):
    bl_idname = "VIEW3D_PT_tr_thickness"
    bl_label = tr_ui_consts['workflow']['thickness']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_thickness="tr_operators.thickness")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'thickness'
                and not context.scene.ufit_circums_highlighted
                and context.scene.ufit_device_type == 'transradial')
