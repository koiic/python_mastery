'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
'''

from typing import List


def containsDuplicate(nums: List[int]) -> bool:

	return len(set(nums)) < len(nums)
	# if len(list(set(nums))) == len(nums):
	#     return False
	# return True
	# for i in range(len(nums)):
	#     if nums[i] in nums[i+1:]:
	#         return True
	# return False

if __name__ == '__main__':
    print(containsDuplicate([1,2,3,4]))