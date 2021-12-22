import math


def findcommon(arr1, arr2):
	dict_ = {i: True for i in arr1}

	print(dict_)

	for j in arr2:
		if dict_.get(j):
			return True
	return False


def findcommon2(arr1, arr2):
	print(set(arr1) and set(arr2))
	if set(arr1) and set(arr2):
		return True
	return False


if __name__ == '__main__':
	# print(findcommon(['a', 'b', 'c', 'x'], ['z', 'y', 'f']))
	print(findcommon2(['a', 'b', 'c', 'x'], ['z', 'y', 'f']))
	print(math.pow(6, 100))
