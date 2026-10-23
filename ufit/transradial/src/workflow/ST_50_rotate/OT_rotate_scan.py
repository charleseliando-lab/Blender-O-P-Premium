from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_rotate import OTSaveRotation


class OTSaveRotationTR(OTBaseTR, OTSaveRotation):
    """Tooltip"""
    bl_idname = "tr_operators.save_rotation"
    bl_label = "Save Rotation"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='rotate')


