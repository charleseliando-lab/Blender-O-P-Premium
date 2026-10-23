from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_milling import OTMillingModel


class OTMillingModelTR(OTBaseTR, OTMillingModel):
    """Tooltip"""
    bl_idname = "tr_operators.milling_model"
    bl_label = "CNC Milling"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='milling_model')

