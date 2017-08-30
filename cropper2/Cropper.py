# Catsymptote
# 21.12.16 - 00:00


# For file lists
from os import listdir
from os.path import isfile, isdir, join

# For image processing
from PIL import Image

# Folder Registry Names (discontinued)
#from folderRegistry import foldRegReturn


# Global variables
inputFolder  = "input"
outputFolder = "output"
# Under development:
#totalPics = 0


# Functions selection differet crop coordinates for different folders
# Kill with fire
# ------------------------------------------------------------
#"S1", 0, 0, 1920, 1080
def foldS1 ():
    print ("hi")

def foldS2 ():
    print ("hi")

def folderReg (folderName):
    print ("hi")
# ------------------------------------------------------------


# Make a list of files in "input" folder
def fileList (folderName):
    #mypath = "input" # Use folderName instead of mypath
    #fileList = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    fileList = [f for f in listdir(join(inputFolder, folderName))
        if isfile(join(join(inputFolder, folderName), f))]
    # Two lines above can (and maybe should) be in a single (long) line
    print ("\n------------------------------------------------------------")
    print ("fileList:\t" + str(fileList))
    print ("------------------------------------------------------------")
    return fileList


def foldList ():
    #inputFolder = "input" # Main input folder
    folderList = [f for f in listdir(inputFolder) if isdir(join(inputFolder, f))]
    #print ("folderList:\t" + str(folderList))
    return folderList


def cropCoords (folderName):
    # Temporary function. Will be expanded upon later.
    # Generate coords based on folderName in folder reg
    if (folderName == "S1"):
        coords = [0, 0, 1920, 1080]
    elif (folderName == "S2"):
        coords = [1920, 0, 3840, 1080]
    elif (folderName == "TV1"):
        coords = [899, 162, 1304, 882]
    elif (folderName == "TV2"):
        coords = [2819, 162, 3224, 882]
    elif (folderName == "TVF1"):
        coords = [674, 1, 1246, 1017]
    elif (folderName == "TVF2"):
        coords = [2594, 1, 3166, 1017]
    else:
        coords = [0, 0, 10, 10]
    return coords


# Do the cropping of the image and save it in the "output" folder
def cropper (fileName, coords, folderName):
    imageInName  = join(inputFolder, folderName) + "\\" + fileName
    imageOutName = join(outputFolder, folderName) + "\\" + fileName
    img = Image.open(imageInName)
    #img.crop((0, 0, 1920, 1080)).save("output\\" + fileName)
    img.crop(coords).save(imageOutName) # Might work. Otherwise, use below
    #img.crop((coords[0], coords[1], coords[2], coords[3])).save("output\\" + fileName)
    print ("ImageName\t" + imageInName)
    #totalPics += 1


# Test if image is too small for specified cropping
def imgTest (fileName, folderName):
    imageName = join(inputFolder, folderName) + "\\" + fileName
    img = Image.open(imageName)
    w, h = img.size
    if (w >= 1920 and h >= 1080):
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
		or  fileName[-4:] == ".bmp"
        or  fileName[-4:] == ".BMP"
        ):
        return True
    else:
        print ("Error:\t\tFile format not recognized as image format\n")
        return False


# Nothing, currently
def absTest ():
    return False




# ------------------------------------------------------------
# Here dis shit dat happens, m8

def fileController (folderName):
    listOfFiles = fileList(folderName)
    #listOfFiles = fileList("input") # Put folderName here
    #print ("Cur. foldName:\t" + folderName)
    #print ("listOfFiles:\t" + str(listOfFiles))
    #print ("^length^\t" + str(len(listOfFiles)))


    # tests go here, and stuffs
    # if tests; go on, if not tests; abort
    if (absTest ()):
        # Absolute tests
        print("Error: List is disfunctional")
    else:
        for x in range(len(listOfFiles)):
            #print ("File Name\t" + str(listOfFiles[x]))
            if (fileNameTest(listOfFiles[x])):
                if (imgTest(listOfFiles[x], folderName)):
                    cropper (listOfFiles[x], cropCoords (folderName), folderName)


def folderController ():
    folderList = foldList()
    print ("folderList:\t" + str(folderList))
    print ("############################################################")
    print ("############################################################\n")
    for i in range (len(folderList)):
        fileController (folderList[i])

folderController()
#print ("\nPics cropped:\t" + str(totalPics))
#input("Press enter and exit")
input ()
#mep = input()
#print (mep)

# Gives error message, but Idgaf
#print (input("Click Enter to exit\n"))
