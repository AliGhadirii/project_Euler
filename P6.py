def P6(n):
    ans = 0
    for i in range(1,n+1):
        for j in range(i+1, n+1):
            ans += 2 * i * j
    return ans
print(P6(100))