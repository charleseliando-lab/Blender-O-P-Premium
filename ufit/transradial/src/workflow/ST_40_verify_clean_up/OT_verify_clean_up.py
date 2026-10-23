from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_clean_up import (OTApproveCleanUp, OTHighlightNonManifold, OTFillNonManifold,
                                                      OTDeleteNonManifold)


class OTHighlightNonManifoldTR(OTBaseTR, OTHighlightNonManifold):
    """Tooltip"""
    bl_idname = "tr_operators.highlight_non_manifold"
    bl_label = "Highlight Non Manifold"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='highlight_non_manifold')


class OTFillNonManifoldTR(OTBaseTR, OTFillNonManifold):
    """Tooltip"""
    bl_idname = "tr_operators.fill_non_manifold"
    bl_label = "Fix Non Manifold"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='fill_non_manifold')


class OTDeleteNonManifoldTR(OTBaseTR, OTDeleteNonManifold):
    """Tooltip"""
    bl_idname = "tr_operators.delete_non_manifold"
    bl_label = "Delete Non Manifold"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='delete_non_manifold')
    

class OTApproveCleanUpTR(OTBaseTR, OTApproveCleanUp):
    """Tooltip"""
    bl_idname = "tr_operators.approve_clean_up"
    bl_label = "Approve Clean Up"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='verify_clean_up')
