bl_info = {
    "name": "Print A Button",
    "blender": (3, 0, 0),
    "category": "Object",
}
import sys
import bpy
import importlib

sys.path.append(r"E:\nabtew\3d\intern\QT5\file\file_manager")

import core
importlib.reload(core)
import app_v4

class Launch_UI(core.QtWindowEventLoop):
    bl_idname = "wm.file_manager"
    bl_label = "Run"
    
    def __init__(self):
        super().__init__(app_v4.App)

class OBJECT_OT_RUN(bpy.types.Operator):
    bl_idname = "object.file_manager"
    bl_label = "Run"
    bl_description = "File Manager"

    def execute(self, context):
        
        return {'FINISHED'}

class OBJECT_PT_RunPanel(bpy.types.Panel):
    bl_idname = "FM_PT_print_a_panel"
    bl_label = "File Manager Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'File Manager'

    def draw(self, context):
        layout = self.layout
        layout.operator("wm.file_manager", text="Run")


def register():
    bpy.utils.register_class(Launch_UI)
    bpy.utils.register_class(OBJECT_OT_RUN)
    bpy.utils.register_class(OBJECT_PT_RunPanel)


def unregister():
    bpy.utils.unregister_class(Launch_UI)
    bpy.utils.unregister_class(OBJECT_OT_RUN)
    bpy.utils.unregister_class(OBJECT_PT_RunPanel)

if __name__ == "__main__":
    register()