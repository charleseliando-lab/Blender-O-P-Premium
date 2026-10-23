from ....base.src.operators.core.OT_base import OTBase
from ..transradial_constants import tr_path_consts, tr_ui_consts, tr_operator_consts


class OTBaseTR(OTBase):
    def get_path_consts(self):
        return tr_path_consts

    def get_ui_consts(self):
        return tr_ui_consts

    def get_operator_consts(self, operator_name):
        operator_vars = tr_operator_consts.get(operator_name)
        if operator_vars:
            return operator_vars
        else:
            raise ValueError(f"Unknown operator name: {operator_name}")

