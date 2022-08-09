from PIL import Image
import numpy
import matplotlib as plt
im = Image.open('strose_pennant.jpg', 'r')
width, height = im.size
new_image = Image.new(im.mode, im.size)
new_pixel_map = new_image.load()
for x in range(width):
    for y in range(height):
        pixel = im.getpixel((x,y))
        new_pixel = sum(pixel) // len(pixel)  # integer division
        new_pixel = tuple([new_pixel]*3)
        new_pixel_map[x,y] = new_pixel
im.show()
new_image.show()
pass