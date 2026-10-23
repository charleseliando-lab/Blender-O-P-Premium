from .....base.src.ui.base.UI_cutout import UICutoutSelection
from ...transradial_constants import tr_ui_consts


class UICutoutSelectionTR(UICutoutSelection):
    bl_idname = "VIEW3D_PT_tr_cutout_selection"
    bl_label = tr_ui_consts['workflow']['cutout_selection']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_cutout_selection="tr_operators.cutout_selection")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'cutout_selection'
                and not context.scene.ufit_circums_highlighted
                and context.scene.ufit_device_type == 'transradial')
