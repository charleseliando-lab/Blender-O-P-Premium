from .....base.src.operators.base.OT_start import OTStartModeling, OTStartFromExisting
from ..OT_Base_TR import OTBaseTR


class OTStartModelingTR(OTBaseTR, OTStartModeling):
    """Tooltip"""
    bl_idname = "tr_operators.start_modeling"
    bl_label = "Create New"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='start_modeling')


class OTStartFromExistingTR(OTBaseTR, OTStartFromExisting):
    """Tooltip"""
    bl_idname = "tr_operators.start_from_existing"
    bl_label = "Resume"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='start_from_existing')
