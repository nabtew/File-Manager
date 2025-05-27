import bpy
import sys
import os
import logging
from PySide6 import QtWidgets 
from PySide6 import QtCore 
from PySide6 import QtGui

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class QtWindowEventLoop(bpy.types.Operator):
	"""docstring for QtWindowEventLoop"""
	bl_idname = 'screen.qt_event_loop'
	bl_label = 'Qt Event Loop'

	def __init__(self, widget, *args, **kwargs):
		self._widget = widget 
		self._args = args
		self._kwargs = kwargs
		
	def modal(self, context, event): 
		wm = context.window_manager

		if not self.widget.isVisible():
			# if widget is closed
			logger.debug('finish modal operator')
			wm.event_timer_remove(self._timer)
			return {'FINISHED'}
		else:
			logger.debug('process the events for Qt window')
			self.event_loop.processEvents()
			self.app.sendPostedEvents(None, 0)

		return {'PASS_THROUGH'}

	def execute(self, context): 
		self.report({'INFO'}, 'execute operator')
		print('----')

		self.app = QtWidgets.QApplication.instance()

		if not self.app:
			self.app = QtWidgets.QApplication(sys.argv)

		if 'stylesheet' in self._kwargs:
			stylesheet = self._kwargs['stylesheet']
			self.set_stylesheet(self.app, stylesheet)

		self.event_loop = QtCore.QEventLoop()
		self.widget = self._widget(*self._args, **self._kwargs)

		logger.debug(self.app)
		logger.debug(self.widget)

		# run modal 
		wm = context.window_manager
		self._timer = wm.event_timer_add(1 / 120, window=context.window)
		context.window_manager.modal_handler_add(self)
		print('finished')
		self.widget.show()

		return {'RUNNING_MODAL'}

	def set_stylesheet(self, app, filepath): 
		file_css = QtCore.QFile(filepath)
		if file_css.exists():
			file_css.open(QtCore.QFile.ReadOnly)
			stylesheet = QtCore.QTextStream(file_css).readAll()
			app.setStyleSheet(stylesheet)
			file_css.close()


def register(): 
	bpy.utils.register_class(QtWindowEventLoop)


def unregister():
	bpy.utils.unregister_class(QtWindowEventLoop)
		