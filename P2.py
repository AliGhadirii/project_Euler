def P2(n):
    sum = 2
    a=1
    b=2
    while True:
        i = a+b
        if i > n:
            break
        if i % 2 == 0:
            sum += i
        a = b
        b = i
    return sum
print(P2(4000000))