""" Implementing the fibonnaci sequence with recursion """

def get_fib(position):
  if position <= 0:
    return -1
  if position == 1:
    return 0
  elif position == 2:
    return 1
  else:
    return get_fib(position - 1) + get_fib(position - 2)

""" Implementing the fibonacci sequence with dynamic programming """


# def fibonacci(position):
#   fib_array = [0,1]
#   if position < 0:
#     print ('invalid')
#   elif position <= len(fib_array):
#     return fib_array[position - 1]

#   else:
#     temp_fib = fibonacci(position + 1) + fibonacci(position - 2)
#     fib_array.append(temp_fib)
#     return temp_fib


if __name__ == '__main__':
  # Test cases
  print (get_fib(10))
  print (get_fib(11))
  print (get_fib(0))
  # print(fibonacci(3))