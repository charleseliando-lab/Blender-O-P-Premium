from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_connector import OTImportConnector
from .....base.src.operators.core.alignment import import_connector


class OTImportConnectorTR(OTBaseTR, OTImportConnector):
    """Tooltip"""
    bl_idname = "tr_operators.import_connector"
    bl_label = "Import Connector"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='import_connector')

    def main_func(self, context):
        import_connector(context,
                         self.get_path_consts(),
                         context.scene.tr_connector_type,
                         context.scene.tr_amputation_side)
