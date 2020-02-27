def missing_number(array):
      new_list = []
  if(len(array) == 1 and array[0] > 1):
    return array[0] - 1
  
  if 1 not in array:
    return 1
  for num in array:
    if num < 0:
      del num
    elif num+1 not in array:
      new_list.append(num + 1)
  return min(new_list)
      

    
def missing_number_sort(array):
  if(len(array) == 1 and array[0] > 1):
    return array[0] - 1
  
  sorted_array = sorted(array)
  if 1 not in sorted_array:
    return 1
  for num in sorted_array:
    if num < 0:
      del num
    elif num+1 not in array:
      return num + 1
  return 1


def missing_num(array):
  # make array contain only positive numbers
  # negative numbers or 0 does not affect the result
  array = [a for a in array if a >= 1]
  # remove duplicates
  array = list(set(array))
  # if after removing duplicates and negatives, array is empty,
  # return 1
  if not array:
    return 1
  # sort array for looping below
  array.sort()
  
  min_num = min(array)
  max_num = max(array) or 1
  if max_num < 1:
    return 1
  for i in range(1,max_num):
    if array[i-1] == i:
      continue
    else:
      return i
  return max_num + 1




print(missing_num([4,1,2]))
print(missing_num([2]))
print(missing_num([-90000,-99999,-6,-7, -11, 1, 2, 5]))
print(missing_num([-90000,-99999,-6,-7, -11]))
print(missing_num([1, 3, 6, 4, 1, 2]))
print(missing_num([3]))
print(missing_num([-1, -3, 1]))
print(missing_num([1,4,5,2,3]))
print('>>>>>')


print(missing_number([-90000,-99999,-6,-7, -11]))
print(missing_number([1, 3, 6, 4, 1, 2]))
print(missing_number([3]))
print(missing_number([-1, -3, 1]))
print(missing_number([1,4,5,2,3]))