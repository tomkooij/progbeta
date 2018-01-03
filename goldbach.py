def isPrime(n):
    """primality check"""
    if n == 1:
        return False
    if n == 2:
        return True
    if not n % 2:
        return False
    for divisor in range(3, int(n**0.5) + 1, 2):
        if not n % divisor:
            return False
    return True


def primes(n):
    """yield primes up to n"""
    for i in range(n):
        if isPrime(i):
            yield i


N = 1000
primes = list(primes(N))

goldbach = {}
for p1 in primes:
    for p2 in primes:
        goldbach[p1 + p2] = (p1, p2)

for n in range(4, N + 1, 2):
    a, b = goldbach[n]
    print(f'{n} = {a} + {b}')
