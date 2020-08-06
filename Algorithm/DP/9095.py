T=int(input())
dp=[1, 2, 4]

for i in range(T):
    n=int(input())

    if len(dp)>=n:
        print(dp[n-1])
    else:
        for i in range(n-len(dp)):
            index=len(dp)
            dp.append(dp[index-3]+dp[index-2]+dp[index-1])
        print(dp[n-1])