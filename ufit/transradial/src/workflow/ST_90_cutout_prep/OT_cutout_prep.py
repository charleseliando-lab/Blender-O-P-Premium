from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_cutout import OTCutoutPlane


class OTCutoutPlaneTR(OTBaseTR, OTCutoutPlane):
    """Tooltip"""
    bl_idname = "tr_operators.cutout_plane"
    bl_label = "Create Cutout Plane"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='cutout_prep')


# class OTStraightCutoutPlaneTR(OTBaseTR, OTCutoutPlane):
#     pass

