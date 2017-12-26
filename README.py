idx     = 0
resDict = {}
rList   = open("words.txt", "r").read().split(" ")

for i, elem in enumerate(rList):
    if elem in resDict.keys():
      tmp = resDict.get(elem)
      tmp[1] += 1
      resDict[elem] = tmp
    else:
      resDict.update( { elem: [idx,1] } )
      idx+=1

        
# -*- coding: utf-8 -*-
import math
from PIL import Image

im = Image.open( "westbrook.png" )
rgb_im = im.convert('RGB')
pixels = rgb_im.load() # create the pixel map

# Get Size
width, height = im.size
print(width, height)


for i in range(im.size[0]):
    for j in range(im.size[1]):
        r, g, b = rgb_im.getpixel((i, j))
        pixels[i,j] = ( math.floor(r/2), math.floor(g/2), math.floor(b/2))

rgb_im.show()

        
