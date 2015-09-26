__author__ = 'Fabian'



import requests
import json
import os
import sys
from .paths import tempfolder

def convert(mod):
    return mod

def download(mod, target = tempfolder, callback = None):
    url = mod["releases"][0]["files"][0]["mirror"]
    if not url:
        url = mod["releases"][0]["files"][0]["url"]
    if not url:
        raise Exception("Cannot find download link for mod.")
    filename = os.path.basename(url).split("?")[0]
    r = requests.get(url, stream=True)
    location = os.path.join(target, filename)
    with open(location, 'wb') as t:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                t.write(chunk)
                if callback:callback(r)
    return location

class ModIndex():
    website = r"http://api.factoriomods.com"
    def __init__(self):
        print("Retrieving Mods Index", end="",flush=True)
        self._retrieve()
        print(" Done!")
    def _retrieve(self):
        r = requests.get(self.website+"/mods")

        mods = json.loads(r.content.decode())
        self.index = {}
        self.list = []
        for mod in mods:
            mod = convert(mod)
            self.index[mod['title']] = mod
            self.list.append(mod)
            print(".",end="", flush=True)

ModIndex = ModIndex()



