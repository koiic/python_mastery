""" Implementing the fibonnaci sequence with recursion """
from collections import defaultdict

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


def fibonacci(position):
  fib_array = [0,1]
  if position < 0:
    print ('invalid')
  elif position <= len(fib_array):
    return fib_array[position - 1]

  else:
    temp_fib = fibonacci(position + 1) + fibonacci(position - 2)
    fib_array.append(temp_fib)
    return temp_fib

#memoization
def fib_memo(n, d):
  
  d[n] += 1
  if n == 0:
    return 0, d
  if n == 1:
    return 1, d
  n1, _ = fib_memo(n-1, d)
  n2, _ = fib_memo(n-2, d)
  return n1 + n2, d


if __name__ == '__main__':
  # Test cases
  print (get_fib(10))
  print (get_fib(11))
  print (get_fib(0))
  print(fib_memo(10, defaultdict(int)))