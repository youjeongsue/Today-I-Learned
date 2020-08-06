N=int(input())
dp=[0,1,1,1,1,1,1,1,1,1]

for _ in range(N-1):
    temp=dp[:]
    dp[0]=temp[1]
    dp[9]=temp[8]
    for i in range(1,9):
        dp[i]=temp[i-1]+temp[i+1]

print(sum(dp)%1000000000)