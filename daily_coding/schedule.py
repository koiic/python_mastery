import threading

import schedule


def add():
	sum = 2 + 2
	print(sum)
	return sum


# def scheduler(f, n):
# 	schedule.every(n).seconds.do(f())


if __name__ == '__main__':
	threading.Timer(1, add()).start()
