
""" Binary Search Implementation"""

def binary_search_while_loop(input_array, value):

  start = 0
  end = len(input_array) - 1

  while start <= end:
    mid = int((start + end)/2)
    if value == input_array[mid]:
        return mid
    elif value < input_array[mid]:
        end = mid - 1
    elif value > input_array[mid]:
        start = mid + 1
  return -1


def binary_search_for_loop(input_array, value):

  start = 0
  end = len(input_array) - 1

  for x in input_array:
    mid = int((start + end)/2)
    if value == input_array[mid]:
        return mid
    elif value < input_array[mid]:
        end = mid - 1
    elif value > input_array[mid]:
        start = mid + 1
  print("\nElement not found!")
  return -1


def binary_search_recursion(input_array, value, start, end):
  if end >= 1:
    mid = int(start + (end - 1)/2)

    if value == input_array[mid]:
      return mid

    elif value < input_array[mid]:
        end = mid - 1
        return binary_search_recursion(input_array, value, start, end)

    else:
        start = mid + 1
        return binary_search_recursion(input_array, value, start, end)

  else:
    return -1


if __name__ == '__main__':
  print(binary_search_while_loop([1,3,9,11,15,19,29], 1))
  print(binary_search_for_loop([1,3,9,11,15,19,29], 29))
  array = [1,3,9,11,15,19,29]
  start = 0
  end = len(array) - 1
  value = 1
  print(binary_search_recursion(array, value, start, end))


