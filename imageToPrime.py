from pathlib import Path
from PIL import Image, ImageOps

import sys

# improper arguments
if (len(sys.argv) != 2 ):
    print('Command use should follow the form "python imageToPrime.py <imagePath>" ')
    exit()

filePath = sys.argv[1]
img = Image.open(filePath)

img.show()

# applying grayscale method
gray_image = ImageOps.grayscale(img)
gray_image.show()



