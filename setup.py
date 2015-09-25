import os
import shutil
import cx_Freeze
import sys
import platform

folder = "%d.%d" % (sys.version_info.major, sys.version_info.minor)
if sys.platform.startswith("win"):
    gui = "Win32GUI"
    if platform.architecture()[0] == "64bit":
        folder = "exe.win-amd64-" + folder
    else:
        folder = "exe.win32-" + folder
    win = True
else:
    gui = None
    folder = "exe.linux-x86_64-" + folder
    win = False

def installfile(name):
    dst = os.path.join('build', folder)
    print('copying', name, '->', dst)
    if os.path.isdir(name):
        dst = os.path.join(dst, name)
        #print dst+" folder"
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(name, dst)
    elif os.path.isfile(name):
        shutil.copy(name, dst)
        #print name+" file"
    else:
        print(('Warning, %s not found' % name))

lib = True

EXE = cx_Freeze.Executable(
    script="run_fm.py",
    targetName="FactorioManager.exe",
    icon="icon.ico",
    compress=True,
    #base=gui,
    appendScriptToLibrary=lib,
    appendScriptToExe=not lib
)
exes = [EXE]

cx_Freeze.setup(
    name="Factorio Manager",
    version="1",
    description="Manager for Factorio Mods",
    executables=exes,
    options={"build_exe": {"excludes": ["OpenGL",
                                        "numpy",
                                        "tkinter",
                                        "tcl",
                                        "pyreadline",
                                        "unittest",
                                        "distutils",
                                        "win32api",
                                        "pywintypes33",
                                        "win32con",
                                        "pydoc",
                                        "cython"],
                           "packages": ["FactorioManager"],
                           "optimize": 2,
                           "compressed": 1,
                           "create_shared_zip": 1,
                           "include_in_shared_zip": 1,
        }
    }
)

extra_data = []
for data in extra_data:
    installfile(data)
print("done")
