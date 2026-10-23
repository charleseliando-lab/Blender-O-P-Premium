from .....base.src.ui.base.UI_pull_bottom import UIPullBottom
from ...transradial_constants import tr_ui_consts


class UIPullBottomTR(UIPullBottom):
    bl_idname = "VIEW3D_PT_tr_pull_bottom"
    bl_label = tr_ui_consts['workflow']['pull_bottom']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       "tr_operators.pull_bottom",
                       "tr_operators.pull_bottom_done")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'pull_bottom'
                and not context.scene.ufit_circums_highlighted
                and context.scene.ufit_device_type == 'transradial')
