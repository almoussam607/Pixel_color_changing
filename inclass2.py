from time import sleep
from threading import *
from concurrent.futures import ThreadPoolExecutor
tresults=[]
def listworker(worklist):
    total = 0
    for item in worklist:
        sleep(0.5)
        total += item
    #print(f'thread-name:{current_thread().getName()}:{total}')
    #tresults.append(total)
    return total
if __name__ == "__main__":
    overall_total = 0
    ftrs = []
    tp = ThreadPoolExecutor(10)
    for t in range(10):
        test_list = [x for x in range(t*10, (t+1)*10)]
        # create thread and pass it list
        #thd = Thread(target=listworker,args=(test_list,))
        #thd.start()
        #thread_list.append(thd)
        f = tp.submit(listworker, test_list)
        ftrs.append(f)
        print(test_list)
    # if polling - put following block in while-loop
    for task in ftrs:
        overall_total += task.result()
    #for task in thread_list:
    #    task.join()
    #for val in tresults:
    #    overall_total += val
   # print(f'Overall Total: {overall_total}')

