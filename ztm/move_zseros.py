from typing import List


def move_zeros(nums: List[int]) -> None:
	
	zero_count = 0
	index_list = []
	
	for i in range(len(nums)):
		if nums[i] == 0:
			zero_count += 1
		index_list.append(i)
	for i in sorted(index_list, reverse=True):
		del nums[i]
		nums.append(0)
	return nums

if __name__ == '__main__':
    print(move_zeros([0,1,0,3,12]))


