import math

# def sieve_of_eratosthenes(max_integer):
#     sieve = [True for _ in range(max_integer + 1)]
#     sieve[0:1] = [False, False]
#     for start in range(2, max_integer + 1):
#         if sieve[start]:
#             for i in range(2 * start, max_integer + 1, start):
#                 sieve[i] = False
#     primes = []
#     for i in range(2, max_integer + 1):
#         if sieve[i]:
#             primes.append(i)
#     return primes


def check_prime(num):
    if num == 1 or num == 0:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        k = int(input())
        print(check_prime(k))
