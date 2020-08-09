import math

def is_prime(n):
    flg = True
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            flg = False
            break
    return flg

def nthprime(n):
    counter = 0
    ans = 0
    i = 2
    while True:
        if (is_prime(i)):
            counter += 1
            ans = i
            i += 1
        else:
            i += 1
        if counter == n:
            return ans

print(nthprime(10001))