from .....base.src.ui.base.UI_finish import UIExportDevice
from ...transradial_constants import tr_ui_consts


class UIExportSocketTR(UIExportDevice):
    bl_idname = "VIEW3D_PT_tr_export_socket"
    bl_label = tr_ui_consts['workflow']['export']['ui_name']

    def draw(self, context):
        self.draw_base(context,
                       ot_export_device="tr_operators.export_socket")

    @classmethod
    def poll(cls, context):
        return (context.scene.ufit_active_step == 'export'
                and not context.scene.ufit_circums_highlighted
                and context.scene.ufit_device_type == 'transradial')
