def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def find_primes():
    primes = []
    num = 1001
    while len(primes) < 100:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

print(find_primes())