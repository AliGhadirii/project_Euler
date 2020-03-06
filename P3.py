import math
def isprime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return 0
    else:
        return 1


def P3(n):
    max = n
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0 and isprime(i):
            max = i
    return max

from time import time
t0 = time()
print(P3(600851475143))
print("spent time : ", time()-t0)
