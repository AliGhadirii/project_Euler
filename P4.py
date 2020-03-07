from math import *
def ispol(n):
    if str(n)[::-1] == str(n):
        return 1
    return 0

def P4(n):
    max = 0
    for i in range(int(pow(10, n-1)), int(pow(10, n) - 1) + 1):
        for j in range(int(pow(10, n-1)), int(pow(10, n) - 1) + 1):
            if ispol(i * j) and i * j > max:
                max = i * j
    return  max

print(P4(3))

