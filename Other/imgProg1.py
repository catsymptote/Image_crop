from PIL import Image

# Create the image
img = Image.new("RGB", (640, 480), (0, 0, 255))

# Loops through all the pixels
for x in range(640):
    for y in range(480):

        # Make dat art tho
        img.putpixel( (x,y), ( int(x/3), int(y/2), int((x+y)/6) ) )


        """
        # Make some random lines
        if (x == y):
            img.putpixel((x,y), (0, 255, 0))
        if ((640-x) == (480-y)):
            img.putpixel((x,y), (255, 0, 0))
        if ((640-x) == (y)):
            img.putpixel((x,y), (0, 255, 0))
        if ((x) == (480-y)):
            img.putpixel((x,y), (255, 0, 0))
        """



"""
# Make some random pixels
img.putpixel((123,246), (255, 0, 0))
img.putpixel((125,246), (255, 0, 0))
img.putpixel((123,248), (255, 0, 0))
img.putpixel((125,248), (255, 0, 0))
"""

img.save("image.png", "PNG")

img.show()
