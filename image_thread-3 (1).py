from PIL import Image
from concurrent.futures import ThreadPoolExecutor

im = Image.open('strose_pennant.jpg', 'r')
width, height = im.size
new_image = Image.new(im.mode, im.size)
new_pixel_map = new_image.load()

def pixel_color(pixel):
    l3 = []
    for i in pixel:
        new_pixel = sum(i) // len(i)  # integer division
        new_pixel = tuple([new_pixel]*3)
        l3.append(new_pixel)
    return l3

if __name__ == "__main__":

    futures = []
    pool = ThreadPoolExecutor(width)
    l1 = []

    for x in range(width):
        for y in range(height):
            pixel1 = im.getpixel((x, y))
            l1.append(pixel1)
        v = pool.submit(pixel_color, l1)
        l1 = []
        futures.append(v)
    print(futures)

    cl = 0
    newlist = []
    for task in futures:
        newlist = task.result()
        rw = 0
        for pixel2 in newlist:
            new_pixel_map[cl, rw] = pixel2
            rw += 1
        cl += 1

im.show()
new_image.show()




