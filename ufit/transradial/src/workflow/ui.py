import bpy
from .ST_0_start.UI_start_modeling import UIStartModelingTR
from .ST_10_import_scan.UI_import_scan import UIImportScanTR
from .ST_20_indicate.UI_indicate_patella import UIMoveScanTR
from .ST_30_clean_up.UI_clean_up import UICleanUpScanTR
from .ST_40_verify_clean_up.UI_verify_clean_up import UIVerifyCleanUpTR
from .ST_50_rotate.UI_rotate_scan import UIRotateTR
from .ST_60_circumferences.UI_circumferences import UIAddCircumferencesTR, UICircumferencesTR
from .ST_70_push_pull_smooth.UI_push_pull_smooth import UIPushPullRegionsTR
from .ST_80_pull_bottom.UI_pull_bottom import UIPullBottomTR
from .ST_90_cutout_prep.UI_cutout_prep import UICutoutPrepTR
from .ST_100_cutout.UI_cutout import UICutoutTR
from .ST_105_cutout_selection.UI_cutout_selection import UICutoutSelectionTR
from .ST_110_scale.UI_liner_scaling import UIScaleScanTR
from .ST_120_verify_scaling.UI_verify_scaling import UIVerifyScalingTR
from .ST_125_socket_milling.UI_socket_milling import UISocketMillingTR
from .ST_130_milling_model.UI_milling_model import UIMillingModelTR
from .ST_130_thickness.UI_thickness import UIThicknessTR
from .ST_132_custom_thickness.UI_custom_thickness import UICustomThicknessTR
from .ST_135_flare.UI_flare import UIFlareTR
from .ST_140_verify_socket.UI_verify_socket import UIVerifySocketTR
from .ST_150_import_connector.UI_import_connector import UIImportConnectorTR
from .ST_160_align.UI_alignment import UIMoveConnectorTR
from .ST_170_transition.UI_transition_connector import UITransitionConnectorTR
from .ST_180_export.UI_export_socket import UIExportSocketTR
from .ST_190_finish.UI_finish import UIFinishedTR


def register():
    bpy.utils.register_class(UIStartModelingTR)
    bpy.utils.register_class(UIImportScanTR)
    bpy.utils.register_class(UIMoveScanTR)
    bpy.utils.register_class(UICleanUpScanTR)
    bpy.utils.register_class(UIVerifyCleanUpTR)
    bpy.utils.register_class(UIRotateTR)
    bpy.utils.register_class(UICircumferencesTR)
    bpy.utils.register_class(UIAddCircumferencesTR)
    bpy.utils.register_class(UIPushPullRegionsTR)
    bpy.utils.register_class(UIPullBottomTR)
    bpy.utils.register_class(UICutoutPrepTR)
    bpy.utils.register_class(UICutoutTR)
    bpy.utils.register_class(UICutoutSelectionTR)
    bpy.utils.register_class(UIScaleScanTR)
    bpy.utils.register_class(UIVerifyScalingTR)
    bpy.utils.register_class(UISocketMillingTR)
    bpy.utils.register_class(UIMillingModelTR)
    bpy.utils.register_class(UIThicknessTR)
    bpy.utils.register_class(UICustomThicknessTR)
    bpy.utils.register_class(UIFlareTR)
    bpy.utils.register_class(UIVerifySocketTR)
    bpy.utils.register_class(UIImportConnectorTR)
    bpy.utils.register_class(UIMoveConnectorTR)
    bpy.utils.register_class(UITransitionConnectorTR)
    bpy.utils.register_class(UIExportSocketTR)
    bpy.utils.register_class(UIFinishedTR)


def unregister():
    bpy.utils.unregister_class(UIStartModelingTR)
    bpy.utils.unregister_class(UIImportScanTR)
    bpy.utils.unregister_class(UIMoveScanTR)
    bpy.utils.unregister_class(UICleanUpScanTR)
    bpy.utils.unregister_class(UIVerifyCleanUpTR)
    bpy.utils.unregister_class(UIRotateTR)
    bpy.utils.unregister_class(UICircumferencesTR)
    bpy.utils.unregister_class(UIAddCircumferencesTR)
    bpy.utils.unregister_class(UIPushPullRegionsTR)
    bpy.utils.unregister_class(UIPullBottomTR)
    bpy.utils.unregister_class(UICutoutPrepTR)
    bpy.utils.unregister_class(UICutoutTR)
    bpy.utils.unregister_class(UICutoutSelectionTR)
    bpy.utils.unregister_class(UIScaleScanTR)
    bpy.utils.unregister_class(UIVerifyScalingTR)
    bpy.utils.unregister_class(UISocketMillingTR)
    bpy.utils.unregister_class(UIMillingModelTR)
    bpy.utils.unregister_class(UIThicknessTR)
    bpy.utils.unregister_class(UICustomThicknessTR)
    bpy.utils.unregister_class(UIFlareTR)
    bpy.utils.unregister_class(UIVerifySocketTR)
    bpy.utils.unregister_class(UIImportConnectorTR)
    bpy.utils.unregister_class(UIMoveConnectorTR)
    bpy.utils.unregister_class(UITransitionConnectorTR)
    bpy.utils.unregister_class(UIExportSocketTR)
    bpy.utils.unregister_class(UIFinishedTR)
