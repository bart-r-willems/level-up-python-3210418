def main():
  assert get_prime_factors(630) == [2, 3, 3, 5, 7]
  assert get_prime_factors(13) == [13]
  print(get_prime_factors(1969))


def get_prime_factors(n: int) -> list:
  '''Return a list of the prime factors of n'''

  primes = [2]
  result = []
  x = n
  p = 2
  while True:
    if x % p == 0:
      result.append(p)
      x = x // p
    else:
      # try next prime
      p = p + 1
      while not all(p % x for x in primes):
        p += 1
      primes.append(p)
    if x == 1:
      return result


main()