import random
from PIL import Image, ImageDraw

image = Image.open("perun.jpg")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

# print(width, height)
reverse_image = Image.new('RGB', (width, height))
for i in range(width):
    for j in range(height):
        pix = image.getpixel((i, j))
        reverse_image.putpixel((width - i - 1, j), pix)

reverse_image.save("perun_reversed.jpg")
reverse_image.show("perun_reversed.jpg")

