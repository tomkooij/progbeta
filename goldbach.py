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


N = 1000


# lookup-table for all possible sums of primes
primes = [x for x in range(N) if isPrime(x)]
sum_of_primes = {}
for p1 in primes:
    for p2 in primes:
        sum_of_primes[p1 + p2] = (p1, p2)

for n in range(4, N + 1, 2):
    a, b = sum_of_primes[n]
    print(f'{n} = {a} + {b}')
