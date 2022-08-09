import threading
import time

class MyThread(threading.Thread):
    def run(self):
        sleep(5)
        for x in range(3):
            print(f'Hi form child thread')


a = MyThread()
a.start()
a.join()
print('Good Bye')


    futures = []
    pool = ThreadPoolExecutor(width)
    l1 = []

    for x in range(width):
        for y in range(height):
            pixel1 = im.getpixel((x, y))
            l1.append(pixel1)
        v = pool.submit(pixel_color, l1)
        futures.append(v)
    print(futures)

cl = 0
newlist = []
for task in ftrs:
    newlist = task.result()
    rw = 0
    for pixel2 in newlist:
        new_pixel_map[rw, cl] = pixel2
        rw += 1
    cl += 1
