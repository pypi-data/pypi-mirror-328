import os
from muphyn.packages.core.base.managers import ManagerMetaClass

class DirectoryManager(metaclass=ManagerMetaClass):

    def __init__(self) -> None:
        # Init base working directory
        self.base_working_directory = os.getcwd()
        
        # Init current working directory
        self.current_working_directory = self.base_working_directory

    def reset_working_directory(self):
        # Test if Base Working Directory exists
        if not os.path.exists(self.base_working_directory):
            raise Exception(f"Base Working Directory doesn't exists: {self.base_working_directory}")
            
        # Change working directory
        self.set_working_directory(self.base_working_directory)

    def set_working_directory(self, new_wd_path: str):
        # Test IF new path exists & path is dir
        if os.path.exists(new_wd_path) and os.path.isdir(new_wd_path):
            # Test IF new path is relative
            if not os.path.isabs(new_wd_path):
                # Build absolute path from relative path
                new_wd_path = os.path.join(self.current_working_directory, new_wd_path)

            # Change working directory
            os.chdir(new_wd_path)
            self.current_working_directory = os.getcwd().replace("\\", "/")
        else:
            raise Exception(f"New Working Directory doesn't exists : {new_wd_path}")
