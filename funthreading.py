# import threading
import concurrent.futures
import time

start = time.perf_counter()


def do_something(sconds):
    print(f'Sleeping {sconds} second...')

    time.sleep(sconds)

    print('Done Sleeping...\n')



with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    # for result in results:
    #     print(result())
    #
finish = time.perf_counter()

print(f' Finished in {round(finish - start, 2)} second(s)')

# threads = []

# for _ in range(10):
#     t1 = threading.Thread(target=do_something, args=[1.5])
#     t1.start()
#     threads.append(t1)
#
# for thread in threads:
#     thread.join()

7yuy