
import os
import getpass

def getCurrentUser() -> str:

    # Get the username from the OS
    currentUser = os.getenv('USER') or os.getenv('LOGNAME') or os.getenv('USERNAME')

    # If the above methods fail, you can try using getpass
    if currentUser is None:
        try:
            currentUser = getpass.getuser()
        except Exception as e:
            currentUser = "Unknown"

    return currentUser