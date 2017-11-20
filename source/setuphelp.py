import sys
from cx_Freeze import setup, Executable

base = None

executables = [
    Executable('help.py', base=base)
]

setup(
    name="mtaobao_help",
    version="2.0",
    description="hunterhug",
    executables=executables
)
