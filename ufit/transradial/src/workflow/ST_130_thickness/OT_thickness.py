from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_thickness import OTThickness


class OTThicknessTR(OTBaseTR, OTThickness):
    """Tooltip"""
    bl_idname = "tr_operators.thickness"
    bl_label = "Choose Print Thickness"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='thickness')
