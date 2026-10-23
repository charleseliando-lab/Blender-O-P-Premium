from .....base.src.ui.base.UI_cutout import UICutout
from ...transradial_constants import tr_ui_consts


class UICutoutTR(UICutout):
    bl_idname = "VIEW3D_PT_tr_cutout_plane"
    bl_label = tr_ui_consts['workflow']['cutout']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_cutout="tr_operators.cutout")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'cutout'
                and not context.scene.ufit_circums_highlighted
                and context.scene.ufit_device_type == 'transradial')