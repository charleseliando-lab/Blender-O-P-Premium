from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_finish import OTExportDevice


class OTExportSocketTR(OTBaseTR, OTExportDevice):
    """Tooltip"""
    bl_idname = "tr_operators.export_socket"
    bl_label = "Export Socket"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='export')
