from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_custom_thickness import OTCustomThickness, OTCustomThicknessDone


class OTCustomThicknessTR(OTBaseTR, OTCustomThickness):
    """Tooltip"""
    bl_idname = "tr_operators.custom_thickness"
    bl_label = "Apply Thickness"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='custom_thickness')


class OTCustomThicknessDoneTR(OTBaseTR, OTCustomThicknessDone):
    """Tooltip"""
    bl_idname = "tr_operators.custom_thickness_done"
    bl_label = "Next"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='custom_thickness_done')
