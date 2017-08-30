from os import listdir
from os.path import isfile, join

# mypath = "G:\Google Drive\EDU\_Projects\Image Crop"


def fileList ():
    mypath = "input"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles



print (fileList())
