import math

def is_prime(n):
    flg = True
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            flg = False
            break
    return flg

def P10():
    sum = 0
    for i in range(2,2000001):
        if is_prime(i):
            sum += i
    return sum

print(P10())
