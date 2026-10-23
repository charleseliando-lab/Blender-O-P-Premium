import bpy
from .....base.src.operators.core.OT_base import OTBase
from .....base.src.operators.core.sculpt import reinforce_trimline, reinforce_trimline_done


class OTReinforceTrimline(OTBase):
    @classmethod
    def poll(cls, context):
        active_object = context.active_object
        if active_object is not None \
                and active_object.type == 'MESH' \
                and active_object.mode == 'OBJECT' \
                and active_object.name == 'uFit':
            return True

    def main_func(self, context):
        # execute func
        reinforce_trimline(context)


class OTReinforceTrimlineDone(OTBase):
    @classmethod
    def poll(cls, context):
        return True

    def main_func(self, context):
        reinforce_trimline_done(context)