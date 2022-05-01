from pathlib import Path
from PIL import Image, ImageOps

import sys

SCALE_FACTOR = 0.1
# exit on improper arguments
if (len(sys.argv) != 2 ):
    print('Command use should follow the form "python imageToPrime.py <imagePath>" ')
    exit()

# shades = '1723456908'
shades = '1230'
filePath = sys.argv[1]
img = Image.open(filePath)

# applying grayscale method
gray_image = ImageOps.grayscale(img)

#reduce then pallete
rThenPal = gray_image.resize((int(gray_image.width * 2* SCALE_FACTOR), int(gray_image.height * SCALE_FACTOR)))
rThenPal = rThenPal.convert('P', palette=Image.ADAPTIVE, colors=len(shades))

intString = ""
outputFile = open("asciiArt.txt", "w")
imgPixels = rThenPal.load()
for rowNum in range(rThenPal.height):
    for colNum in range(rThenPal.width):
        outputFile.write(shades[imgPixels[colNum, rowNum]])
        intString += shades[imgPixels[colNum, rowNum]]
    outputFile.write("\n")
outputFile.close()

startNum = int(intString)

