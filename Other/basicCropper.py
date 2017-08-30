from PIL import Image

img = Image.open("cropme.png")

w, h = img.size
img.crop((899, 162, 1304, 882)).save("cropped.png")


# Start: 899, 162
# Stop: 1303, 881 (+1)
