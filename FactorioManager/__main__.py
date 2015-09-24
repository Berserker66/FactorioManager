__author__ = 'Fabian'
from .paths import get_instances, tempfolder
from .remoteapi import ModIndex, download
from .ModFile import ModFile

print("Temp:", tempfolder)

instances = get_instances()
print("Remote Modlist:")
print(", ".join(ModIndex.index))

for mod in ModIndex.list:
    print("-----------------------------------------------------")
    loc = download(mod)
    modfile = ModFile(loc)
    check = modfile.check()
    if check == True:
        print("Mod downloaded and checked.")
    else:
        print(check)