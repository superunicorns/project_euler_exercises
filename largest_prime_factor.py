# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

num = 600851475143


def largest_prime_factor(num):
    factors = []

    while num % 2 == 0:
        factors.append(2)
        num //= 2

    divider = 3
    while divider * divider <= num:
        while num % divider == 0:
            factors.append(divider)
            num //= divider

        divider += 2

    if num > 2:
        factors.append(num)

    return factors[-1]


print(str(largest_prime_factor(num)))