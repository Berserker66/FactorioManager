__author__ = 'Fabian'
import zipfile

class ModFile():
    def __init__(self, path):
        self.path = path

    def check(self):
        try:
            zip = zipfile.ZipFile(self.path)
            zip.testzip()
            files = zip.namelist()
            info = False
            for file in files:
                if "info.json" in file:
                    info = True
            if not info:
                raise FileNotFoundError("Cannot find info.json in modfile.")
        except Exception as e:
            return e
        else:
            return True
    @staticmethod
    def checkfile(path):
        mod = ModFile(path)
        return mod.check()