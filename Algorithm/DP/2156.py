n = int(input())
wine = []
dp = [0]*n

for _ in range(n):
    wine.append(int(input()))

dp[0] = wine[0]
dp[1] = wine[0] + wine[1]

for i in range(2,n):
    dp[i] = wine[i] + dp[i-2]

print(dp)