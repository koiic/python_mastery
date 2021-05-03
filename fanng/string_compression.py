''':cvar
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?
'''
from typing import List


def compress(chars: List[str]) -> int:
	if len(chars) == 1:
		return 1
	char_to_compare = chars[0]
	store = f'{char_to_compare}1'
	for i in range(1, len(chars)):
		print(i)
		if chars[i] == char_to_compare:
			store = store.replace(store[len(store) - 1], str(int(store[len(store) - 1]) + 1))
		else:
			char_to_compare = chars[i]
			store += f'{char_to_compare}1'

	print(store, '==============')


def maxScoreSightseeingPair(A: List[int]) -> int:
	list_max = [get_score(A, i) for i in range(len(A) - 1)]
	return max(list_max)


def get_score(arr, i):
	max_pair = 0
	for j in range(i+1, len(arr)):

		score = (arr[i] + arr[j]) + (i - j)
		if score > max_pair:
			max_pair = score

	return max_pair

def max_score2(arr):
	max_count = 0
	count = 0
	i = count
	j = i + 1
	while count < len(arr)-1:
		if j < len(arr):
			score = arr[i] + arr[j] + i - j
			if score > max_count: max_count = score
			count += 1
			i = count
			j = i + 1

	return max_count




def max_score(arr):
	max_count = 0
	for i in range(len(arr) - 1):
		for j in range(i + 1, len(arr)):
			score = arr[i] + arr[j] + i - j
			if score > max_count: max_count = score
		return max_count

if __name__ == '__main__':
	# print(compress(["a","a","a","b","b","c","c","c","c","a","a"]))
	# print(compress(["a", 'a', 'b', 'a', 'a']))
	# print(maxScoreSightseeingPair([8, 1, 5, 2, 6]))
	# print(maxScoreSightseeingPair([2, 2, 2]))
	# print(max_score([2, 2, 2]))
	print(max_score2([8,1,5,2,6]))
