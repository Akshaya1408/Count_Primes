def countprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_less_than_n(n):
    count = 0
    for i in range(2, n):
        if countprime(i):
            count += 1
    return count

num = int(input())
print(count_primes_less_than_n(num)) 