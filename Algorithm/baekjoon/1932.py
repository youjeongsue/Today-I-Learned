n = int(input())
#dp[i][j]: i, j에 도착 했을 때의 최대값
#dp[i][j]: max(dp[i-1][j-1], dp[i+1][j]) + dp[i][j]
inputs = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n) for _ in range(n)]

dp[0][0]=inputs[0][0]

for i in range(n):
    for j in range(i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + inputs[i][j]

print(max(dp[-1]))