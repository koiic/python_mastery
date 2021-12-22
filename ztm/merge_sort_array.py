# merge two array in a sorted order
def merge_list(list1, list2):
	merged_list = []
	list1_first = list1[0]
	list2_first = list2[0]
	i = 0
	j = 0

	# for i in range(len(list1)+1):
	# 	print(list1[i])
	# 	if not list2[i] or list1[i] < list2[i]:
	# 		merged_list.append(list1.pop(list1[i]))
	# 	else:
	# 		merged_list.append(list2.pop(list2[i]))

	while len(list1) or len(list2):
		# print(list1_first, list2_first)
		if list1[i] < list2[j]:
			merged_list.append(list1[i])
			# list1_first = list1[i]
			i += 1
		else:
			merged_list.append(list2[j])
			# list2_first = list2[j]
			j += 1
		print(j, '---<><>', list2[j])

	return merged_list

def push_first(item, merge):
	merge.append(item)


if __name__ == '__main__':
	merge_list([0, 3, 4, 31], [4, 6, 30])
