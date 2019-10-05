def is_prime(number):
  if number <= 1:
    return False

  for factor in range(2, number):
    # print('===', factor, number)
    if number % factor == 0:
      return False

  return True


def is_prime_fast(number):
  import math
  if number <= 1:
    return False
  if number != 2 and number % 2 == 0:
    return False
  for factor in range(3, int(math.sqrt(number))+ 1):
    if number % factor == 0:
      return False
  return True

def get_primes(n_start, n_end):
  for number in range(n_start, n_end):
    if is_prime_fast(number):
      print(number)


def mersenne_number(p):
  return 2**p - 1


def lucas_lehmer(p):
    array = [4]
    for n in range(1, p-1):
        number = (((array[n - 1]) ** 2) -2) % mersenne_number(p)
        array.append(number)
    return array


def ll_prime(p):
    # true_tuple = []
    true_tuple = [(number, 1) if lucas_lehmer(number)[number-2] == 0 else (number, 0) for number in get_primes(3, 65)]
    # for number in get_primes(3, 65):
    #   if lucas_lehmer(number)[number-2] == 0:
    #     true_tuple.append((number, 1))
    #   true_tuple.append((number, 0))
    return true_tuple




# get_primes(3, 65)
# for i in range(500):
#   assert is_prime_fast(i) == is_prime(i)
# print(is_prime_fast(3))
# print('====>>>>', mersenne_number(17))
# print('====>>>>', lucas_lehmer(17))
if __name__ == '__main__':
  
  print('====>>>>', ll_prime(17))