from .....base.src.ui.base.UI_push_pull_smooth import UIPushPullRegions
from ...transradial_constants import tr_ui_consts


class UIPushPullRegionsTR(UIPushPullRegions):
    bl_idname = "VIEW3D_PT_tr_push_pull_regions"
    bl_label = tr_ui_consts['workflow']['push_pull_smooth']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_push_pull_region="tr_operators.push_pull_region",
                       ot_smooth_region="tr_operators.smooth_region",
                       ot_free_sculpt_checkpoint="tr_operators.free_sculpt_checkpoint",
                       ot_push_pull_smooth_done="tr_operators.push_pull_smooth_done")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'push_pull_smooth'
                and not context.scene.ufit_circums_highlighted
                and context.scene.ufit_device_type == 'transradial')
