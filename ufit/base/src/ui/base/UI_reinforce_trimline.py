import bpy
from .....base.src.ui.utils.general import UFitPanel
from .....base.src.ui.utils.general import get_standard_navbox


class UIReinforceTrimline(UFitPanel, bpy.types.Panel):
    def draw_base(self, context, ot_reinforce_trimline, ot_reinforce_trimline_done):
        scene = context.scene
        layout = self.layout

        box0 = layout.box()
        box0_row0 = box0.row()
        box0_row0.prop(scene, 'ufit_reinforce_trimline_distance', expand=True)

        box1 = layout.box()
        box1_row0 = box1.row()
        box1_row0.prop(scene, 'ufit_reinforce_trimline_extra_thickness', expand=True)

        box2 = layout.box()
        box2_row0 = box2.row()
        box2_row0.operator(ot_reinforce_trimline, text='Apply Reinforce Trimline')

        get_standard_navbox(self.layout, "ufit_operators.prev_step", ot_reinforce_trimline_done)