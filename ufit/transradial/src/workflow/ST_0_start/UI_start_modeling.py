from .....base.src.ui.base.UI_start import UIStartModeling
from ...transradial_constants import tr_ui_consts


class UIStartModelingTR(UIStartModeling):
    bl_idname = "VIEW3D_PT_tr_start_modeling"
    bl_label = tr_ui_consts['workflow']['start']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_start="tr_operators.start_modeling",
                       ot_start_from_existing="tr_operators.start_from_existing")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'start'
                and context.scene.ufit_device_type == 'transradial')
