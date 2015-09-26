__author__ = 'Fabian'


import unittest

broken_mods = {"5dim mod", "Air Filtering", "canInsert"}


class TestRemoteAPI(unittest.TestCase):
    indextestfields = ["title", "contact", "name", "homepage", "author"]
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
            modname = mod["title"]
            with self.subTest(modname):
                print("Testing mod {} of {}.".format(i + 1, len(remoteapi.ModIndex.list)))
                loc = remoteapi.download(mod)
                modfile = ModFile(loc)
                ret = modfile.check()
                if ret != True:
                    if modname in broken_mods:
                        self.skipTest("Mod {} is expected to fail: {}".format(modname,ret))
                    raise ret
                elif modname in broken_mods:
                    self.fail("Mod {} is repaired, but still listed as broken.".format(modname))
                else:
                    with self.subTest(modname + " Sanity Check"):
                        info = modfile.get_info()
                        for field in self.indextestfields:
                            self.assertEqual(info[field], mod[field])
