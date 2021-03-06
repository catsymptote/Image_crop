# Catsymptote
# 12.12.16 - 03:48


# For file lists
from os import listdir
from os.path import isfile, join

# For image processing
from PIL import Image


# Make a list of files in "input" folder
def fileList ():
    mypath = "input"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


# Do the cropping of the image and save it in the "output" folder
def cropper (fileName):
    img = Image.open("input\\" + fileName)
    img.crop((899, 162, 1304, 882)).save("output\\" + fileName)


# Test if image is too small for specified cropping
def imgTest (fileName):
    img = Image.open("input\\" + fileName)
    w, h = img.size
    if (w > 1304 and h > 882):
        return True
    else:
        return False


# Check if the file type is okay
def fileNameTest(fileName):
    #print (fileName[-4:])
    if (    fileName[-4:] == ".png"
        or  fileName[-4:] == ".PNG"
        or  fileName[-4:] == ".jpg"
        or  fileName[-4:] == ".JPG"
        ):
        return True
    else:
        print ("File format not recognized as image format\n")
        return False


# Nothing, currently
def absTest ():
    return False



# Here dis shit dat happens, m8
listOfFiles = fileList()
print (listOfFiles)
print (len(listOfFiles))


# tests go here, and stuffs
# if tests; go on, if not tests; abort
if (absTest ()):
    # Absolute tests
    print("Error: List is disfunctional")
else:
    for x in range(len(listOfFiles)):
        print (listOfFiles[x])
        if (fileNameTest(listOfFiles[x])):
            if (imgTest(listOfFiles[x])):
                cropper (listOfFiles[x])
