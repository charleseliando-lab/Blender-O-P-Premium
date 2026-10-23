from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_scale import OTApproveScaling


class OTApproveScalingTR(OTBaseTR, OTApproveScaling):
    """Tooltip"""
    bl_idname = "tr_operators.approve_scaling"
    bl_label = "Approve Scaling"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='verify_scaling')
