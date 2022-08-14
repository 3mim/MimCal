import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {'include_files':['C:/Users/MORTEZA/Documents/pythonCode/MimCal/old-versian/fonts'],"includes": ["tkinter","customtkinter",],"excludes": ["_distutils_hack", "cffi", "concurrent", 
                                  "curses",
                                  "email",
                                  "html",
                                  "http", 
                                  "lib2to3",
                                  "logging",
                                  "msilib",
                                  "multiprocessing",
                                  "numpy",
                                  "PIL",
                                  "pkg_resources",
                                  "pycparser",
                                  "pydoc_data",
                                  "PyInstaller",
                                  "setuptools",
                                  "test",
                                  "test",
                                  "win32ctypes",
                                  "xml",
                                  "xmlrpc"],
                                  
                                  "optimize": 2}
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "mimcal",
    version = "0.1",
    description = "trading application",
    options = {"build_exe": build_exe_options},
    executables = [Executable("mimcal.py", base = base,shortcutName="MimCal",shortcutDir="DesktopFolder",icon="logo.ico")]
    
    )
