import bpy
from .....base.src.ui.utils.general import UFitPanel, get_standard_navbox, get_label_multiline


class UIStartModeling(UFitPanel, bpy.types.Panel):
    def draw_base(self, context, ot_start, ot_start_from_existing):
        scene = context.scene
        layout = self.layout

        box0 = layout.box()
        box0_row0 = box0.row()
        box0_row1 = box0.row()
        box0_row0.operator(ot_start)
        box0_row1.operator(ot_start_from_existing)

        nav_box = layout.box().row()
        nav_box.operator("ufit_operators.prev_step", text="Back")


class UIImportScan(UFitPanel, bpy.types.Panel):
    def draw_base(self, context, ot_import_scan):
        scene = context.scene
        layout = self.layout

        row0 = layout.row()
        row0.label(text="Medical Device ID")

        row1 = layout.row()
        row1.prop(scene, "ufit_medical_device", text="")

        row2 = layout.row()
        row2.label(text="Scan Properties")

        row3 = layout.row()
        row3.prop(scene, 'ufit_file_type', expand=True)

        row4 = layout.row()
        row4.prop(scene, 'ufit_scan_scale_size', expand=True)

        # row5 = layout.row()
        # row5.operator(ot_import_scan)

        # nav_box = layout.box().row()
        # nav_box.operator("ufit_operators.prev_step", text="Back")

        # separator
        layout.row().separator()  # spacer
        layout.row().separator()  # spacer

        row5 = layout.row()
        row5_box0 = row5.box()
        get_label_multiline(
            context=context,
            text='When clicking Next your scan will be downloaded from the platform. '
                 'Please note this might take a while...',
            parent=row5_box0
        )

        get_standard_navbox(self.layout, "ufit_operators.prev_step", ot_import_scan)




