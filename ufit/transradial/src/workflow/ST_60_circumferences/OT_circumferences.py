from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_circumferences import (
    OTCircumference,
    OTCircumferencesCalc,
    OTCircumferencesDone,
    OTCircumferencesHighlight
)


class OTCircumferenceTR(OTBaseTR, OTCircumference):
    """Tooltip"""
    bl_idname = "tr_operators.add_circumference"
    bl_label = "Add"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='circumference_add')


class OTCircumferencesCalcTR(OTBaseTR, OTCircumferencesCalc):
    """Tooltip"""
    bl_idname = "tr_operators.circumferences_calc"
    bl_label = "Calculate Circumferences"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='circumferences_calc')


class OTCircumferencesDoneTR(OTBaseTR, OTCircumferencesDone):
    """Tooltip"""
    bl_idname = "tr_operators.circumferences_done"
    bl_label = "Done"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='circumferences_done')


class OTCircumferencesHighlightTR(OTBaseTR, OTCircumferencesHighlight):
    """Tooltip"""
    bl_idname = "tr_operators.circumferences_highlight"
    bl_label = "Highlight Circumferences"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='circumferences_highlight')
