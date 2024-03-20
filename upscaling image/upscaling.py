import random
from PIL import Image, ImageDraw
import numpy as np

image = Image.open("perun.jpg")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

print(width, height)

upscaled_image = Image.new('RGB', (width * 2, height * 2))



temp = [[0 for i in range(width)]for j in range(height)]
for j in range(height):
    for i in range(width):
        pix = image.getpixel((i, j))
        temp[j][i] = pix
print(temp)

for j in range(1, height*2, 2):
    for i in range(1, width*2, 2):
        upscaled_image.putpixel((i-1, j-1), temp[int(j/2)][int(i/2)])
        upscaled_image.putpixel((i, j-1), temp[int(j/2)][int(i/2)])
        upscaled_image.putpixel((i-1, j), temp[int(j/2)][int(i/2)])
        upscaled_image.putpixel((i, j), temp[int(j/2)][int(i/2)])
        

upscaled_image.save("perun_upscaled.jpg")
upscaled_image.show("perun_upscaled.jpg")