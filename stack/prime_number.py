def is_prime(number):
  if number == 1:
    return False

  for factor in range(2, number):
    if number % factor == 0:
      return False

  return True

def print_primes(n):
  for number in range(1, n):
    if is_prime(number):
      print(f'{number} is prime')


print_primes(100)