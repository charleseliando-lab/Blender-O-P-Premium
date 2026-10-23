from bpy_extras.io_utils import ImportHelper
from .core.OT_base import OTBase
from .core.platform import set_workspace, platform_login


class OTSetWorkspace(OTBase, ImportHelper):
    """Tooltip"""
    bl_idname = "ufit_operators.set_workspace"
    bl_label = "Choose Workspace"
    bl_options = {"REGISTER", "UNDO"}

    filename_ext = ".."
    use_filter_folder = True

    @classmethod
    def poll(cls, context):
        # always make it possible to select a workspace
        return True

    def execute(self, context):
        return self.execute_base(context,
                                 'set_workspace')

    def main_func(self, context):
        set_workspace(context, self.filepath)


class OTPlatformLogin(OTBase):
    """Tooltip"""
    bl_idname = "ufit_operators.platform_login"
    bl_label = "Login"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if context.scene.ufit_user \
                and context.scene.ufit_password\
                and context.scene.ufit_workspace:
            return True

    def execute(self, context):
        return self.execute_base(context,
                                 'platform_login')

    def main_func(self, context):
        platform_login(context)
