__author__ = 'Fabian'

import sys
import appdirs
import os
import shutil
join = os.path.join

directories = appdirs.AppDirs("FactorioManager", "", roaming=True)

configpath = join(directories.user_config_dir, "config.cfg")
tempfolder = appdirs.user_cache_dir("FactorioManager", "", opinion=False)

assert(tempfolder != directories.user_config_dir)

if not os.path.exists(directories.user_config_dir):
    os.mkdir(directories.user_config_dir)

def get_instances():
    paths = set()
    if sys.platform.startswith("win"):#check for installed factorio
        factorioappdata = join(appdirs.user_config_dir("Factorio", "", roaming=True), "mods")
        if os.path.exists(factorioappdata):
            paths.add(factorioappdata)
    #TODO add configured paths
    return paths

mods_folders = get_instances()

def clean():
    if os.path.exists(tempfolder):
        for file_object in os.listdir(tempfolder):
            file_object_path = os.path.join(tempfolder, file_object)
            try:
                if os.path.isfile(file_object_path):
                    os.unlink(file_object_path)
                else:
                    shutil.rmtree(file_object_path)
            except PermissionError:
                pass
    else:
        os.mkdir(tempfolder)

clean()