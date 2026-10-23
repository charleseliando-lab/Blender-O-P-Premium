from ..OT_Base_TR import OTBaseTR
from .....base.src.operators.base.OT_flare import OTFlare, OTFlareDone


class OTFlareTR(OTBaseTR, OTFlare):
    """Tooltip"""
    bl_idname = "tr_operators.flare"
    bl_label = "Flare"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='flare')


class OTFlareDoneTR(OTBaseTR, OTFlareDone):
    """Tooltip"""
    bl_idname = "tr_operators.flare_done"
    bl_label = "Done"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return self.execute_base(context,
                                 operator_name='flare_done')
