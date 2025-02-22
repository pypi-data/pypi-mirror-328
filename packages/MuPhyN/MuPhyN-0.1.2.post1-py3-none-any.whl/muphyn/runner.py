#-----------------------------------
# Imports
#-----------------------------------

import ctypes
import logging
import sys
import os
import traceback
from types import TracebackType
from time import sleep
from multiprocessing import freeze_support, Process, Manager
from threading import Thread

from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication

from muphyn.packages.core.base import LogManager
from muphyn.packages.interface.mainwindow import MainWindow
from muphyn.packages.interface.application import LoadingScreen

from muphyn.utils.paths import ROOT_DIR, THEME_PATH
from muphyn.assets import ApplicationIcons

from IPython.core.magic import Magics, line_magic, magics_class
from IPython import get_ipython

def muphyn_excepthook(exc_type: type[BaseException], exc_value: BaseException,
        exc_tb: TracebackType):
    # Save opened project as
    if 'win' in globals():
        global win
        win.backup_save_projects()

    # Format Exception error
    exception = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
    formatted_exception = \
        f"Error while running Muphyn: \n{exception}"

    # Write Error in Log File
    LogManager().error(formatted_exception)

    # Quit Applcation
    QApplication.exit(-1)

#-----------------------------------
# Main method
#-----------------------------------
def run_muphyn(globals_dict = {}):
    #_ = os.system('cls')
    myappid = 'ceref.muphyn.1.2'

    if os.name == 'nt' :
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # Replace excepthook function
    sys.excepthook = muphyn_excepthook

    # Init app
    app = QApplication(sys.argv)

    # Handle dpi change
    app.setAttribute(Qt.ApplicationAttribute.AA_Use96Dpi, True)

    # Init app
    app_icon = QIcon()
    app_icon.addFile(ApplicationIcons.MuphynIcon, QSize(400, 400))
    app.setWindowIcon(app_icon)

    # Init splash screen
    loadingScreen = LoadingScreen()
    loadingScreen.show()

    # Load Style Sheet
    with open(THEME_PATH, "r") as styleSheetFile:
        styleSheetFileStr = styleSheetFile.read().replace("%ROOT_DIR%", ROOT_DIR).replace("\\", "/")
        app.setStyleSheet(styleSheetFileStr)

    # Load all data for the application
    loadingScreen.loadApp(globals_dict)

    # Init Main Window
    win = MainWindow()

    # Add main window object to globals
    globals()["win"] = win

    # Open main window
    loadingScreen.finish(win)
    win.show()

    # Launch Muphyn application
    exit_code = app.exec()

    # Print in log the exit code
    LogManager().set_current_project_id(-1)
    LogManager().info(f"Closing MuPhyN application with code: {exit_code}", is_global_message=True)

    # Closing application
    sys.exit(exit_code)

def filter_local_variables(_global_vars = {}):
    _output = {}

    _excl_list = ['In', 'Out', 'Process', 'Thread', 'TracebackType']

    _type_incl_list = [str, int, float, list, dict, type]

    for _x in [key for key in _global_vars if not key.startswith('_')]:
        if type(_global_vars[_x]) in _type_incl_list and _x not in _excl_list:
            _output.update({_x:_global_vars[_x]})

    return _output

def update_globals(vars, ts = 0.25, linked_process:Process = None):
    if linked_process is None:
        return
    while linked_process.is_alive():
        sleep(ts)
        vars.clear()
        vars.update(filter_local_variables(globals().copy()))
    LogManager().info("Closing globals synchronization thread", is_global_message=True)

def start(data = {}):
    # Freeze support before launching the app
    freeze_support()

    # Init Log Manager
    LogManager(log_level=logging.DEBUG)
    _globals = {}

    if len(data) == 0:
        _globals = Manager().dict()
        _globals.update(filter_local_variables(globals().copy()))
        LogManager().info(f"Getting data from globals: {_globals}", is_global_message=True)

    else:
        _globals.update(filter_local_variables(data))

    # TODO: automatically start MuPhyN by opening a file with the same name as the ipynb file
    # TODO: using the key ['__vsc_ipynb_file__'] in globals()
    # TODO: If no file exists, create it

    LogManager().info("Starting MuPhyN process", is_global_message=True)
    _muphyn_process = Process(target=run_muphyn, args=(_globals,))
    _muphyn_process.start()

    LogManager().info("Creating globals synchronization thread", is_global_message=True)
    update_thread = Thread(target=update_globals, args=(_globals, 0.25, _muphyn_process))
    update_thread.start()

if __name__ == '__main__':
    start()

@magics_class
class MuphynMagics(Magics):

    def __init__(self, shell):
        super(MuphynMagics, self).__init__(shell)
        self.default_runner = self.shell.safe_execfile

    @line_magic
    def muphyn(self, line):
        get_ipython().magic("run -i \"" + ROOT_DIR + "/"+ "runner.py\"")

    @line_magic
    def launch_muphyn(self, line):
        # TODO: find a way to launch the simulation from a magic command
        return

def load_ipython_extension(ipython):
    """ Enables to load the module with %load_ext muphyn """
    ipython.register_magics(MuphynMagics)
