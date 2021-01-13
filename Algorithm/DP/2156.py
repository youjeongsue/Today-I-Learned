n = int(input())
dp = [0]*n
wine = [int(input()) for _ in range(n)]

dp[0] = wine[0]
dp[1] = wine[0] + wine[1]

for i in range(2,n):
    dp[i] = wine[i] + dp[i-2]

print(dp)