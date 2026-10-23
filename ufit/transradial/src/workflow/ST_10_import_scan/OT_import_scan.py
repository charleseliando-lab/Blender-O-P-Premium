from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_import_scan import OTImportScan


class OTImportScanTR(OTBaseTR, OTImportScan):
    """Tooltip"""
    bl_idname = "tr_operators.import_scan"
    bl_label = "Select Scan"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='import_scan')
