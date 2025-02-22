from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QSplashScreen


from muphyn.assets import ApplicationIcons
from muphyn.packages.core.application import BoxesLibrariesManager, SchedulersLibrariesManager
from muphyn.packages.core.base import LogManager, DirectoryManager, GlobalEnvVariablesManager

from ...userdata import UserData

class LoadingScreen(QSplashScreen):

    def __init__(self):
        # Ini logo image
        appLogo = QPixmap(ApplicationIcons.MuphynSplashScreen)

        # Init splash screen
        super().__init__(appLogo, Qt.WindowType.WindowStaysOnTopHint)

    def initManagers(self, globalsDict: dict):
        # Change text
        self.showMessage("Initialization...", Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        # Init Managers
        LogManager().info("Starting MuPhyN application", is_global_message=True)
        GlobalEnvVariablesManager(global_vars=globalsDict)
        DirectoryManager()
        BoxesLibrariesManager()
        SchedulersLibrariesManager()

    def loadLibraries(self):
        # Load already added box libraries
        for box_library in UserData().boxes_libraries :
            BoxesLibrariesManager().add_library(box_library)

        # Load already added schedulers libraries
        for scheduler_library in UserData().schedulers_libraries :
            SchedulersLibrariesManager().add_library(scheduler_library)

        # Load default libraries
        BoxesLibrariesManager().load_libraries()
        SchedulersLibrariesManager().load_libraries()


    def loadUserData(self):
        # Change text
        self.showMessage("Load user data...", Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        # Load User parameters
        UserData("./user_data.yaml")
        UserData().load()

    def loadApp(self, globalsDict: dict):
        # Init Managers
        self.initManagers(globalsDict)

        # Load user data
        self.loadUserData()

        # Load libraries
        self.loadLibraries()