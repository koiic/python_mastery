def two_sum(nums, target):
	for i in range(len(nums) - 1):
		b = target - nums[i]
		if b in nums[i + 1:]:  # check elements in list after current index
			return i, nums.index(b, i + 1)
		# for i in range(len(nums)):
	# 	if nums[i] > x:
	# 		break
	# 	value = x - nums[i]
	# 	# print(mapp.get(value), '******')
	# 	if mapp.get(value) is not None:
	# 		return [i, mapp[value]]
	# 	else:
	# 		mapp[value] = [i, value]
		# print(value, '---')
		# # if mapp.get(i):
		# # 	arr.append(i)
		# # else:
		# # 	mapp[i] = value


if __name__ == '__main__':
	print(two_sum([2, 7, 11, 15], 9))
