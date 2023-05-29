import math


def ehPrimo(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


numPrimos = 0

for i in range(2, 10000):
    if ehPrimo(i):
        numPrimos += 1

print(str(numPrimos))
