from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_clean_up import OTCleanUp


class OTCleanUpTR(OTBaseTR, OTCleanUp):
    """Tooltip"""
    bl_idname = "tr_operators.clean_up"
    bl_label = "Clean Up"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='clean_up')
