from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_indicate import OTMoveScan


class OTMoveScanTR(OTBaseTR, OTMoveScan):
    """Tooltip"""
    bl_idname = "tr_operators.move_scan"
    bl_label = "Move Scan"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='move_scan')
