import time
from multiprocessing import Pool, Process
import random


def f(x):
    return x + x


class Processor(Process):
    def __init__(self, number):
        Process.__init__(self)
        self._number = number

    def run(self):
        sleep = random.randrange(1, 10)
        time.sleep(sleep)
        print(f'Worker {self._number}, slept for {sleep} seconds')


if __name__ == '__main__':
    for i in range(1, 6):
        t = Processor(i)
        t.start()
    # with Pool(5) as p:
    #     print(p.map(f, [1, 2, 3]))
