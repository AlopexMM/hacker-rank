# You need to look for all the numbers that can be divided and from this list
# Find the largest prime number
# Test numbers
# 3
# 10
# 17
# 13195
# 1000000000000
# Test Output
# 5
# 17
# 29

import math


def is_prime(a):
    val = True
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            val = False
    return val


def main():
    n = int(input())

    largest_prime = 1

    for _ in range(n):
        a = int(input())
        sqrt = int(math.sqrt(a)) + 1
        for i in range(1, sqrt):
            if a % i == 0:
                if is_prime(a // i) and a // i > largest_prime:
                    largest_prime = a // i
                    break
                elif is_prime(i):
                    largest_prime = i
        print(largest_prime)


if __name__ == '__main__':
    main()