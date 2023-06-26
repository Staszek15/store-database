from pathlib import Path

import os

cdir = os.getcwd()
print("Current Directory: ", cdir)
print("Parent Directory: ", os.path.dirname(cdir))
