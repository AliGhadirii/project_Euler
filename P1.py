def P1(n):
    sum=0
    for i in range(1,n):
        if (i%3==0 or i%5==0):
            sum += i
    return sum
print(P1(1000))