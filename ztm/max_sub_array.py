'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
from typing import List


def maxSubArray(nums: List[int]) -> int:
	total = 0
	max_ = nums[0]
	for i in nums:
		if total < 0:
			total = 0
		total += i
		if total > max_:
			max_ = total

	return max_

if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))