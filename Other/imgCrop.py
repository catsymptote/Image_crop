import sys



from PIL import Image
im = Image.open('imgFile.png')
pixelMap = im.load()

img = Image.new( im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if 205 in pixelMap[i,j]:
           pixelMap[i,j] = (0,0,0,255)
        pixelsNew[i,j] = pixelMap[i,j]
im.close()
img.show()
img.save("out.tif")
img.close()
