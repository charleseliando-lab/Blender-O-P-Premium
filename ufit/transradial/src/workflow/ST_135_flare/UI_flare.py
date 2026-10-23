from .....base.src.ui.base.UI_flare import UIFlare
from ...transradial_constants import tr_ui_consts


class UIFlareTR(UIFlare):
    bl_idname = "VIEW3D_PT_tr_flare"
    bl_label = tr_ui_consts['workflow']['flare']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_flare="tr_operators.flare",
                       ot_flare_done="tr_operators.flare_done")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'flare'
                and not context.scene.ufit_circums_highlighted
                and context.scene.ufit_device_type == 'transradial')
