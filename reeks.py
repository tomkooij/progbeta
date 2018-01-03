from itertools import tee


def isPrime(n):
    """primality check"""
    if n == 1:
        return False
    if n == 2:
        return True
    if not n % 2:
        return False
    for divisor in range(3, int(n**0.5)+1, 2):
        if not n % divisor:
            return False
    return True


def primes(n):
    """yield primes up to n"""
    for i in range(n):
        if isPrime(i):
            yield i


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def distance_non_primes(n):
    """yield conseq non-primes

    returns a list with (length, start, end) tuples

    """
    return [(second - first - 1, first + 1, second - 1)
            for first, second in pairwise(primes(n))]


assert(len(list(primes(100))) == 25)
assert(max(distance_non_primes(100)) == (7, 90, 96))

length, start, end = max(distance_non_primes(10000))
print(f'blabla {start} eind {end}\n{length}')
