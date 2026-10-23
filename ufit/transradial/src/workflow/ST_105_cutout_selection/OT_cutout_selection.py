from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_cutout import OTCutoutSelection


class OTCutoutSelectionTR(OTBaseTR, OTCutoutSelection):
    """Tooltip"""
    bl_idname = "tr_operators.cutout_selection"
    bl_label = "Perform Cutout"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='cutout_selection')
