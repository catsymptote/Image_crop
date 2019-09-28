# This scipt crops images to the right size for extracting
# the relevant part from Snapchat screenshots taken on the
# Huawei P20 Pro. I.e. remove the black bars.


# https://stackoverflow.com/questions/10825217/edit-rgb-values-in-a-jpg-with-python

# For image handling
from PIL import Image

# For finding the files
from os import listdir
from os.path import isfile, join

# For flushing the print
import sys


# Settings
input_folder = "input"
output_folder = "output"
coords = [0, 0, 1080, 2118]


def get_files(input_folder):
    """ Returns all filenames in given directory """
    onlyfiles = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
    return onlyfiles


def crop(fname, coordinates):
    """ Crops given image file to given coordinates """
    try:
        # Open file
        im = Image.open(input_folder + '\\' + fname)# + '.jpg')
        
        # Make sure the image is of expected size
        width, height = im.size
        if(width != 1080 or height != 2240):
            return None

        # Crop and save file
        im.crop(coordinates).save(output_folder + '\\' + fname, quality=100)
    except:
        return None


# Get and count files
files = get_files(input_folder)
file_count = len(files)

# Loading bar
loading_bar = "##################################################"
loading_section_size = file_count / len(loading_bar)
print(loading_bar)

for i in range(file_count):
    # Crop the file at index i
    crop(files[i], coords)
    
    # Loading bar update
    if(i%loading_section_size >= loading_section_size -1):
        print("#", end="")
        sys.stdout.flush()


print("\n\nDone!\n")