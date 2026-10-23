from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_milling import OTSocketMilling


class OTSocketMillingTR(OTBaseTR, OTSocketMilling):
    """Tooltip"""
    bl_idname = "tr_operators.socket_milling"
    bl_label = "Approve Socket/Milling"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='socket_milling')

