from PIL import Image

img = Image.open("image1.png")

#rgb_img = img.convert('RGB')

for x in range(img.size[0]):
    for y in range(img.size[1]):

        # Inverse colours
        r,g,b = img.getpixel((x, y))
        img.putpixel((x,y), (255-r,255-g,255-b))


        """
        # Switch RGB's
        r,g,b = img.getpixel((x, y))
        img.putpixel((x,y), (b,r,g))
        """

img.show()
