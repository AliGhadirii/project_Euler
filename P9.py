def P9():
    for a in range(1001):
        for b in range (a+1, 1001 - a):
            for c in range(b+1 , 1001 - a - b):
                if a*a + b*b == c*c and a+b+c == 1000:
                    return a*b*c
    return 0

print(P9())

