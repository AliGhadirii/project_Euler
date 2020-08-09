def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def LCM(a, b):
    return (a * b) / gcd(a, b)

def P5():
    ans = 1
    for i in range(1,21):
        ans = LCM(ans, i)
    return ans

print(P5())


