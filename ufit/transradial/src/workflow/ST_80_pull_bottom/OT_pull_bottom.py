from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_pull_bottom import OTPullBottom, OTPullBottomDone


class OTPullBottomTR(OTBaseTR, OTPullBottom):
    """Tooltip"""
    bl_idname = "tr_operators.pull_bottom"
    bl_label = "Pull Bottom"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='pull_bottom')


class OTPullBottomDoneTR(OTBaseTR, OTPullBottomDone):
    """Tooltip"""
    bl_idname = "tr_operators.pull_bottom_done"
    bl_label = "Done"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='pull_bottom_done')

