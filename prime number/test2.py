# Program to implement Solovay-Strassen
# Primality Test
import random

# modulo function for doing binary exponentiation


def modulo(base, exponent, mod):
    x = 1
    y = base
    while (exponent > 0):
        if (exponent % 2 == 1):
            x = (x * y) % mod

        y = (y * y) % mod
        exponent = exponent // 2

    return x % mod

# Find Jacobian symbol of numbers


def calculateJacobian(a, n):

    if (a == 0):
        return 0  # (0/n) = 0

    ans = 1
    if (a < 0):

        # (a/n) = (-a/n)*(-1/n)
        a = -a
        if (n % 4 == 3):

            # (-1/n) = -1 if n = 3 (mod 4)
            ans = -ans

    if (a == 1):
        return ans  # (1/n) = 1

    while (a):
        if (a < 0):

            # (a/n) = (-a/n)*(-1/n)
            a = -a
            if (n % 4 == 3):

                # (-1/n) = -1 if n = 3 (mod 4)
                ans = -ans

        while (a % 2 == 0):
            a = a // 2
            if (n % 8 == 3 or n % 8 == 5):
                ans = -ans

        # swap
        a, n = n, a

        if (a % 4 == 3 and n % 4 == 3):
            ans = -ans
        a = a % n

        if (a > n // 2):
            a = a - n

    if (n == 1):
        return ans

    return 0

# The Solovay- Strassen
# Primality Test


def solovoyStrassen(p, iterations):
    # agar p 2dan kichik bo'lsa = not a prime number
    if (p < 2):
        print(p, "is non-prime number")
        return False
    if (p != 2 and p % 2 == 0):
        print(p, "is non-prime number")
        return False

    for i in range(iterations):
        print(i)

        # Generate a random number a
        a = random.randrange(p - 1) + 1
        jacobian = (p + calculateJacobian(a, p)) % p
        mod = modulo(a, (p - 1) / 2, p)

        if (jacobian == 0 or mod != jacobian):
            print(p, "is non-prime number")
            return False
        else:
            print(p, "is prime number")
    #print(p, "is prime number")
    return True


# Iterate the test 100 times
iterations = 100


def iterate(list):
    for i in list:
        if (solovoyStrassen(i, iterations)):
            print('FINAL', i, "is prime number ")
        else:
            print('FINAL', i, "is non-prime number")


# Test 10 (8-digit) numbers
myList = [10000019, 10000079, 10000103, 10000121, 10000139,
          10000141, 10000169, 10000189, 10000223, 10000229, 10000132]

iterate(myList)
