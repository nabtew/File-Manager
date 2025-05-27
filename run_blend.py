import bpy
import core

class LaunchBuilderUI(core.QtWindowEventLoop):
    bl_idname = "wm.builder"
    bl_label = "Launch Builder"
    
    def __init__(self):
        super().__init__(app_v4.App)