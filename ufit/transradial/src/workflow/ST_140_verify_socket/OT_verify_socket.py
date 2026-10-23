from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_thickness import OTApproveThickness


class OTApproveSocketTR(OTBaseTR, OTApproveThickness):
    """Tooltip"""
    bl_idname = "tr_operators.approve_socket"
    bl_label = "Approve Socket"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='verify_socket')

