__author__ = 'Fabian'

from .paths import get_instances, tempfolder, errorlog, log
from .remoteapi import ModIndex, download
from .shared import is_frozen

DEBUG = True

instances = get_instances()


if is_frozen:
    import sys
    import os
    if os.stat(errorlog).st_size > 10:
        import shutil
        shutil.move(errorlog, errorlog+".temp.txt")
        import webbrowser
        webbrowser.open(errorlog+".temp")
    sys.stderr = open(errorlog, "w")
    sys.stdout = open(log,"w")

if DEBUG:
    import sys
    sys.argv.append(r'factoriomods://eyJpZCI6NTIsInVybCI6Imh0dHA6Ly93d3cuZmFjdG9yaW9tb2RzLmNvbS9tb2RzL2dhbGFjdGljLXRyYWRlLW1vZCIsImNhdGVnb3JpZXMiOlsiZ2FtZXBsYXkiXSwiYXV0aG9yIjoiY29vcG1hc3RlciIsImNvbnRhY3QiOiJjb29wbWFzdGVyMjRAZ21haWwuY29tIiwidGl0bGUiOiJHYWxhY3RpYyBUcmFkZSBNb2QiLCJuYW1lIjoiR2FsYWN0aWNUcmFkZSIsImRlc2NyaXB0aW9uIjoiVGhpcyBtb2QgYWRkcyB0aGUgYWJpbGl0eSB0byBidXkgYW5kIHNlbGwgaXRlbXMgaW4gdGhlIGdhbWUgYXQgbWFya2V0IHByaWNlcy4gWW91IHVubG9jayB0aGUgY2hlc3QgYnkgcmVzZWFyY2hpbmcgbWFya2V0IHRyYWRpbmcgd2hpY2ggY29tZXMgYWZ0ZXIgZWxlY3Ryb25pY3MuIiwiaG9tZXBhZ2UiOiIiLCJyZWxlYXNlcyI6W3siaWQiOjI3OSwidmVyc2lvbiI6IjAuNi41IiwicmVsZWFzZWRfYXQiOiIyMDE1LTA5LTIyVDAwOjAwOjAwLjAwMFoiLCJnYW1lX3ZlcnNpb25zIjpbIjAuMTIueCJdLCJkZXBlbmRlbmNpZXMiOltdLCJmaWxlcyI6W3siaWQiOjI5MywibmFtZSI6IiIsIm1pcnJvciI6bnVsbCwidXJsIjoiaHR0cHM6Ly9kcml2ZS5nb29nbGUuY29tL29wZW4/aWQ9MEIteUZ2YTlidS1SVlJEbENXRVowWm1Oa09WRSJ9LHsiaWQiOjI5MiwibmFtZSI6IiIsIm1pcnJvciI6bnVsbCwidXJsIjoiaHR0cDovL3d3dy5mYWN0b3Jpb2ZvcnVtcy5jb20vZm9ydW0vZG93bmxvYWQvZmlsZS5waHA/aWQ9NjA4MyJ9XX0seyJpZCI6Mjc0LCJ2ZXJzaW9uIjoiMC42LjQiLCJyZWxlYXNlZF9hdCI6IjIwMTUtMDktMjBUMDA6MDA6MDAuMDAwWiIsImdhbWVfdmVyc2lvbnMiOlsiMC4xMi54Il0sImRlcGVuZGVuY2llcyI6W10sImZpbGVzIjpbeyJpZCI6Mjg3LCJuYW1lIjoiIiwibWlycm9yIjpudWxsLCJ1cmwiOiJodHRwOi8vd3d3LmZhY3RvcmlvZm9ydW1zLmNvbS9mb3J1bS9kb3dubG9hZC9maWxlLnBocD9pZD02MDI0In0seyJpZCI6Mjg2LCJuYW1lIjoiIiwibWlycm9yIjpudWxsLCJ1cmwiOiJodHRwczovL2RyaXZlLmdvb2dsZS5jb20vb3Blbj9pZD0wQi15RnZhOWJ1LVJWYmxKRVUwRmtNMDFNWlVrIn1dfSx7ImlkIjoyNzAsInZlcnNpb24iOiIwLjYuMiIsInJlbGVhc2VkX2F0IjoiMjAxNS0wOS0xNVQwMDowMDowMC4wMDBaIiwiZ2FtZV92ZXJzaW9ucyI6WyIwLjEyLngiXSwiZGVwZW5kZW5jaWVzIjpbXSwiZmlsZXMiOlt7ImlkIjoyNzksIm5hbWUiOiIiLCJtaXJyb3IiOm51bGwsInVybCI6Imh0dHBzOi8vZHJpdmUuZ29vZ2xlLmNvbS9vcGVuP2lkPTBCLXlGdmE5YnUtUlZkV05YU0d4amFXeHlUMnMifV19LHsiaWQiOjI2NiwidmVyc2lvbiI6IjAuNi4xIiwicmVsZWFzZWRfYXQiOiIyMDE1LTA5LTEwVDAwOjAwOjAwLjAwMFoiLCJnYW1lX3ZlcnNpb25zIjpbIjAuMTIueCJdLCJkZXBlbmRlbmNpZXMiOltdLCJmaWxlcyI6W3siaWQiOjI3MywibmFtZSI6IiIsIm1pcnJvciI6bnVsbCwidXJsIjoiaHR0cHM6Ly9kcml2ZS5nb29nbGUuY29tL29wZW4/aWQ9MEIteUZ2YTlidS1SVlNERnBjMFpNWjNSaVFtTSJ9XX0seyJpZCI6NjksInZlcnNp')
    print("sys.argv:{}".format(sys.argv))
    print("Temp:", tempfolder)
    print("Remote Modlist:")
    print(", ".join(ModIndex.index))

if len(sys.argv) > 1:
    print(len(sys.argv[1]))
    if sys.argv[1].startswith(r"factoriomods://"):
        mod = sys.argv[1].split(r"//")[1]
        import base64
        mod = base64.b64decode(mod)
        #uri is about to change - wait for that to happen




