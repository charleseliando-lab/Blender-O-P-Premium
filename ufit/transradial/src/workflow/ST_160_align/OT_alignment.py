from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_alignment import OTSaveAlignment


class OTSaveAlignmentTR(OTBaseTR, OTSaveAlignment):
    """Tooltip"""
    bl_idname = "tr_operators.save_alignment"
    bl_label = "Save Alignment"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='align')
