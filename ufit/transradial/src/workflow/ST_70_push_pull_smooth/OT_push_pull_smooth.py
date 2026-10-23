from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_push_pull_smooth import \
    OTPushPullRegion, OTSmoothRegion, OTPushPullSmoothDone, OTFreeSculptCheckpoint


class OTPushPullRegionTR(OTBaseTR, OTPushPullRegion):
    """Tooltip"""
    bl_idname = "tr_operators.push_pull_region"
    bl_label = "Push_Pull"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='push_pull_region')


class OTSmoothRegionTR(OTBaseTR, OTSmoothRegion):
    """Tooltip"""
    bl_idname = "tr_operators.smooth_region"
    bl_label = "Smooth"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='smooth_region')


class OTFreeSculptCheckpointTR(OTBaseTR, OTFreeSculptCheckpoint):
    """Tooltip"""
    bl_idname = "tr_operators.free_sculpt_checkpoint"
    bl_label = "Add Checkpoint"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='free_sculpt_checkpoint')


class OTPushPullSmoothDoneTR(OTBaseTR, OTPushPullSmoothDone):
    """Tooltip"""
    bl_idname = "tr_operators.push_pull_smooth_done"
    bl_label = "Done"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='push_pull_smooth_done')
