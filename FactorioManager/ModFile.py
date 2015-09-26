__author__ = 'Fabian'
import zipfile
import json

class ModFile():
    infolocation = None
    def __init__(self, path):
        self.path = path

    def check(self):
        try:
            with zipfile.ZipFile(self.path) as zip:
                zip.testzip()
                files = zip.namelist()
            info = False
            for file in files:
                if "info.json" in file:
                    info = True
                    self.infolocation = file
                    break
            if not info:
                raise FileNotFoundError("Cannot find info.json in modfile.")
        except Exception as e:
            self.infolocation = False
            return e
        else:
            return True

    def get_info(self):
        if self.infolocation is None:
            self.check()
        elif self.infolocation is False:
            raise ValueError("ModFile {} is invalid - info.json unavailable.".format(self.path))
        with zipfile.ZipFile(self.path) as zip:
            info = zip.read(self.infolocation)
        info = json.loads(info.decode())
        return info

    @staticmethod
    def checkfile(path):
        mod = ModFile(path)
        return mod.check()