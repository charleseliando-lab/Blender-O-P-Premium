import bpy
from .utils.general import UFitPanel


class UIPlatformLogin(UFitPanel, bpy.types.Panel):
    bl_idname = "VIEW3D_PT_ufit_platform"
    bl_label = 'uFit Premium Login'
    # bl_options = {"HIDE_HEADER"}

    def draw(self, context):
        layout = self.layout
        col = layout.row().column()

        # Workspace
        box0 = layout.box()
        box0_row0 = box0.row()
        box0_row0.alignment = 'CENTER'
        box0_row1 = box0.row()
        box0_row1.enabled = False
        box0_row2 = box0.row()
        box0_row0.label(text='Workspace')
        box0_row1.prop(context.scene, "ufit_workspace", text="")
        box0_row2.operator("ufit_operators.set_workspace", text="Choose Workspace")

        # Login
        box1 = layout.box()
        box1_row0 = box1.row()
        box1_row0.alignment = 'CENTER'
        box1_row1 = box1.row()
        box1_row2 = box1.row()
        box1_row3 = box1.row()
        box1_row0.label(text='Premium Login')
        box1_row1.prop(context.scene, "ufit_user")
        box1_row2.prop(context.scene, "ufit_password")
        box1_row3.operator("ufit_operators.platform_login")

    @classmethod
    def poll(cls, context):
        return context.scene.ufit_active_step == 'platform_login'