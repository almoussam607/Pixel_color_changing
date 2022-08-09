import logging
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
im = Image.open('strose_pennant.jpg', 'r')
width, height = im.size
new_image = Image.new(im.mode, im.size)
new_pixel_map = new_image.load()

logging.basicConfig(filename='image_color.log', level=logging.DEBUG,
                    format='%(levelname)s:%(asctime)s:%(message)s')
logger = logging.getLogger("My Logger")

def listworker(work):
    bw = []
    for item in work:
        new_pixel = sum(item) // len(item)  # integer division
        new_pixel = tuple([new_pixel] * 3)
        # new_pixel_map[a, b] = new_pixel
        bw.append(new_pixel)
    return bw



if __name__ == "__main__":

    ftrs = []
    tp = ThreadPoolExecutor(width)
    for x in range(width):
        pixel_list = [im.getpixel((x,y)) for y in range(height)]
        f = tp.submit(listworker, pixel_list)

        ftrs.append(f)

    col = 0
    bw_list = []
    for task in ftrs:
        bw_list = task.result()
        row = 0
        for bw_pixel in bw_list:
            new_pixel_map[col, row] = bw_pixel
            row += 1
        col += 1


im.show()
logger.info("Colorful image is converted into black and white color!".format(new_image.show()))




