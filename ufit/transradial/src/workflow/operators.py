import bpy
from .ST_0_start.OT_start_modeling import OTStartModelingTR, OTStartFromExistingTR
from .ST_10_import_scan.OT_import_scan import OTImportScanTR
from .ST_20_indicate.OT_indicate_patella import OTMoveScanTR
from .ST_30_clean_up.OT_clean_up import OTCleanUpTR
from .ST_40_verify_clean_up.OT_verify_clean_up import (
    OTHighlightNonManifoldTR,
    OTFillNonManifoldTR,
    OTDeleteNonManifoldTR,
    OTApproveCleanUpTR,
)
from .ST_50_rotate.OT_rotate_scan import OTSaveRotationTR
from .ST_60_circumferences.OT_circumferences import (
    OTCircumferenceTR,
    OTCircumferencesCalcTR,
    OTCircumferencesDoneTR,
    OTCircumferencesHighlightTR
)
from .ST_70_push_pull_smooth.OT_push_pull_smooth import (
    OTPushPullRegionTR,
    OTSmoothRegionTR,
    OTFreeSculptCheckpointTR,
    OTPushPullSmoothDoneTR
)
from .ST_80_pull_bottom.OT_pull_bottom import OTPullBottomTR, OTPullBottomDoneTR
from .ST_90_cutout_prep.OT_cutout_prep import OTCutoutPlaneTR
from .ST_100_cutout.OT_cutout import OTCutoutTR
from .ST_105_cutout_selection.OT_cutout_selection import OTCutoutSelectionTR
from .ST_110_scale.OT_liner_scaling import OTLinerScaleTR
from .ST_120_verify_scaling.OT_verify_scaling import OTApproveScalingTR
from .ST_125_socket_milling.OT_socket_milling import OTSocketMillingTR
from .ST_130_milling_model.OT_milling_model import OTMillingModelTR
from .ST_130_thickness.OT_thickness import OTThicknessTR
from .ST_132_custom_thickness.OT_custom_thickness import OTCustomThicknessTR, OTCustomThicknessDoneTR
from .ST_135_flare.OT_flare import OTFlareTR, OTFlareDoneTR
from .ST_140_verify_socket.OT_verify_socket import OTApproveSocketTR
from .ST_150_import_connector.OT_import_connector import OTImportConnectorTR
from .ST_160_align.OT_alignment import OTSaveAlignmentTR
from .ST_170_transition.OT_transition_connector import OTTransitionConnectorTR
from .ST_180_export.OT_export_socket import OTExportSocketTR
from .ST_190_finish.OT_finish import OTTinishTR


def register():
    bpy.utils.register_class(OTStartModelingTR)
    bpy.utils.register_class(OTStartFromExistingTR)
    bpy.utils.register_class(OTImportScanTR)
    bpy.utils.register_class(OTMoveScanTR)
    bpy.utils.register_class(OTCleanUpTR)
    bpy.utils.register_class(OTHighlightNonManifoldTR)
    bpy.utils.register_class(OTFillNonManifoldTR)
    bpy.utils.register_class(OTDeleteNonManifoldTR)
    bpy.utils.register_class(OTApproveCleanUpTR)
    bpy.utils.register_class(OTSaveRotationTR)
    bpy.utils.register_class(OTCircumferenceTR)
    bpy.utils.register_class(OTCircumferencesCalcTR)
    bpy.utils.register_class(OTCircumferencesDoneTR)
    bpy.utils.register_class(OTCircumferencesHighlightTR)
    bpy.utils.register_class(OTLinerScaleTR)
    bpy.utils.register_class(OTApproveScalingTR)
    bpy.utils.register_class(OTSocketMillingTR)
    bpy.utils.register_class(OTMillingModelTR)
    bpy.utils.register_class(OTSmoothRegionTR)
    bpy.utils.register_class(OTPushPullRegionTR)
    bpy.utils.register_class(OTFreeSculptCheckpointTR)
    bpy.utils.register_class(OTPushPullSmoothDoneTR)
    bpy.utils.register_class(OTPullBottomTR)
    bpy.utils.register_class(OTPullBottomDoneTR)
    bpy.utils.register_class(OTCutoutPlaneTR)
    bpy.utils.register_class(OTCutoutTR)
    bpy.utils.register_class(OTCutoutSelectionTR)
    bpy.utils.register_class(OTThicknessTR)
    bpy.utils.register_class(OTCustomThicknessTR)
    bpy.utils.register_class(OTCustomThicknessDoneTR)
    bpy.utils.register_class(OTFlareTR)
    bpy.utils.register_class(OTFlareDoneTR)
    bpy.utils.register_class(OTApproveSocketTR)
    bpy.utils.register_class(OTImportConnectorTR)
    bpy.utils.register_class(OTSaveAlignmentTR)
    bpy.utils.register_class(OTTransitionConnectorTR)
    bpy.utils.register_class(OTExportSocketTR)
    bpy.utils.register_class(OTTinishTR)


def unregister():
    bpy.utils.unregister_class(OTStartModelingTR)
    bpy.utils.unregister_class(OTStartFromExistingTR)
    bpy.utils.unregister_class(OTImportScanTR)
    bpy.utils.unregister_class(OTMoveScanTR)
    bpy.utils.unregister_class(OTCleanUpTR)
    bpy.utils.unregister_class(OTHighlightNonManifoldTR)
    bpy.utils.unregister_class(OTFillNonManifoldTR)
    bpy.utils.unregister_class(OTDeleteNonManifoldTR)
    bpy.utils.unregister_class(OTApproveCleanUpTR)
    bpy.utils.unregister_class(OTSaveRotationTR)
    bpy.utils.unregister_class(OTCircumferenceTR)
    bpy.utils.unregister_class(OTCircumferencesCalcTR)
    bpy.utils.unregister_class(OTCircumferencesDoneTR)
    bpy.utils.unregister_class(OTCircumferencesHighlightTR)
    bpy.utils.unregister_class(OTLinerScaleTR)
    bpy.utils.unregister_class(OTApproveScalingTR)
    bpy.utils.unregister_class(OTSocketMillingTR)
    bpy.utils.unregister_class(OTMillingModelTR)
    bpy.utils.unregister_class(OTSmoothRegionTR)
    bpy.utils.unregister_class(OTPushPullRegionTR)
    bpy.utils.unregister_class(OTFreeSculptCheckpointTR)
    bpy.utils.unregister_class(OTPushPullSmoothDoneTR)
    bpy.utils.unregister_class(OTPullBottomTR)
    bpy.utils.unregister_class(OTPullBottomDoneTR)
    bpy.utils.unregister_class(OTCutoutPlaneTR)
    bpy.utils.unregister_class(OTCutoutTR)
    bpy.utils.unregister_class(OTCutoutSelectionTR)
    bpy.utils.unregister_class(OTThicknessTR)
    bpy.utils.unregister_class(OTCustomThicknessTR)
    bpy.utils.unregister_class(OTCustomThicknessDoneTR)
    bpy.utils.unregister_class(OTFlareTR)
    bpy.utils.unregister_class(OTFlareDoneTR)
    bpy.utils.unregister_class(OTApproveSocketTR)
    bpy.utils.unregister_class(OTImportConnectorTR)
    bpy.utils.unregister_class(OTSaveAlignmentTR)
    bpy.utils.unregister_class(OTTransitionConnectorTR)
    bpy.utils.unregister_class(OTExportSocketTR)
    bpy.utils.unregister_class(OTTinishTR)
