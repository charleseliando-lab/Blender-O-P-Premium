from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_connector import OTTransitionConnector


class OTTransitionConnectorTR(OTBaseTR, OTTransitionConnector):
    """Tooltip"""
    bl_idname = "tr_operators.transition_connector"
    bl_label = "Transition Connector"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='transition')
