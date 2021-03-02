N=int(input())
dp=[1]*10

for _ in range(N-1):
    temp=dp[:]
    for i in range(0,10):
        dp[i]=sum(temp[i:])

print(sum(dp)%10007)