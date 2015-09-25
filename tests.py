__author__ = 'Fabian'


import unittest



class TestRemoteAPI(unittest.TestCase):

    def test_index(self):
        from FactorioManager import remoteapi
        index = remoteapi.ModIndex
        for mod in index.index:
            self.assertTrue(type(mod) is str)
        self.assertTrue(len(index.index)> 1)
        self.index = index

    def test_mod_download(self):
        from FactorioManager import remoteapi
        mod = remoteapi.ModIndex.list[0]
        loc = remoteapi.download(mod)
        from FactorioManager.ModFile import ModFile
        ModFile.checkfile(loc)

    def test_all_mods_integrity(self):
        from FactorioManager import remoteapi
        from FactorioManager.ModFile import ModFile
        for i,mod in enumerate(remoteapi.ModIndex.list):
            with self.subTest(mod["title"]):
                print("Testing mod {} of {}.".format(i, len(remoteapi.ModIndex.list)))
                loc = remoteapi.download(mod)
                ret = ModFile.checkfile(loc)
                if ret != True:
                    raise ret