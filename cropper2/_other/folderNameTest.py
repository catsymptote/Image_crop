from os import listdir
from os.path import isfile, isdir, join

mypath = "input"
#onlyfiles   = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = [f for f in listdir() if isfile(f)]
print (onlyfiles)

#folders     = [f for f in listdir(mypath) if isdir(join(mypath, f))]
folders = [f for f in listdir() if isdir(f)]
print (folders)
