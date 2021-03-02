N=int(input())
dp=[0,1]

for _ in range(0,N-1):
    temp=[0,0]
    temp[0]=dp[0]+dp[1]
    temp[1]=dp[0]
    dp=temp[:]

print(sum(dp))