import time
from pathlib import Path
from PIL import Image, ImageOps

import sys

SCALE_FACTOR = 0.2
# exit on improper arguments
if (len(sys.argv) != 2 ):
    print('Command use should follow the form "python imageToPrime.py <imagePath>" ')
    exit()

shades = '1723456908'
filePath = sys.argv[1]
img = Image.open(filePath)

# img.show()

# applying grayscale method
gray_image = ImageOps.grayscale(img)


#reduce then pallete
rThenPal = gray_image.resize((int(gray_image.height * SCALE_FACTOR), int(gray_image.width * SCALE_FACTOR)))
rThenPal = rThenPal.convert('P', palette=Image.ADAPTIVE, colors=len(shades))


# time.sleep(3)
# # pallete then reduce
# palThenR = gray_image.convert('P', palette=Image.ADAPTIVE, colors=len(shades))
# palThenR = palThenR.resize((int(palThenR.width * SCALE_FACTOR), int(palThenR.height * SCALE_FACTOR)))
# palThenR.show()



outputFile = open("output.txt", "w")
imgPixels = rThenPal.load()
for rowNum in range(rThenPal.height):
    for colNum in range(rThenPal.width):
        outputFile.write(shades[imgPixels[colNum, rowNum]])
    outputFile.write("\n")
outputFile.close()