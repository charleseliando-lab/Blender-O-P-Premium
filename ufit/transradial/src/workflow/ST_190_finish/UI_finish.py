from .....base.src.ui.base.UI_finish import UIFinished
from ...transradial_constants import tr_ui_consts


class UIFinishedTR(UIFinished):
    bl_idname = "VIEW3D_PT_tr_finished"
    bl_label = tr_ui_consts['workflow']['finish']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_restart="tr_operators.restart")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'finish'
                and not context.scene.ufit_circums_highlighted
                and context.scene.ufit_device_type == 'transradial')
