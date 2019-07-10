import cx_Freeze
from cx_Freeze import *

setup (
    name = "Platformer",
    version = "1.0",
    executables = [Executable(platformer.py)]
    )
