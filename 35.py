from math import sqrt

def isprime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    m = int(sqrt(num))
    for i in range(3, m + 1, 2):
        if num % i == 0:
            return False
    return True

def rotations(num):
    s = str(num)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

c = 0
for i in range(2, 1000000):
    if all(isprime(rot) for rot in rotations(i)):
        c += 1

print(c)
