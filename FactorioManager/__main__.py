__author__ = 'Fabian'

from .paths import get_instances, tempfolder
from .remoteapi import ModIndex, download
from .ModFile import ModFile

DEBUG = True

instances = get_instances()

if DEBUG:
    print("Temp:", tempfolder)
    print("Remote Modlist:")
    print(", ".join(ModIndex.index))

    def _debug_download():
        for mod in ModIndex.list:
            print("-----------------------------------------------------")
            loc = download(mod)
            modfile = ModFile(loc)
            check = modfile.check()
            if check == True:
                print("Mod downloaded and checked.")
            else:
                print(check)
    _debug_download()

