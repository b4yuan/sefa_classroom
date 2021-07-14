import time
import multiprocessing
import os


def function1():
    for i in range(1, 10):
        print(i)
        time.sleep(1)
    return 'pp'

def checkfortimeout(func, args=None, timeout=5):
    process1 = multiprocessing.Process(target=time.sleep, args=[timeout])
    if args is None:
        process2 = multiprocessing.Process(target=func)
    else:
        process2 = multiprocessing.Process(target=func, args=[args])

    process1.start()
    process2.start()
    while process1.is_alive():
        if process2.is_alive() is False:
            return
    process2.terminate()
    raise TimeoutError("the program timed out")


if __name__ == '__main__':
    try:
        checkfortimeout(function1)
    except TimeoutError:
        print('there was an error')

    print('end')