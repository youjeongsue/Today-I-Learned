n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + lst[i-1][j-1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])

'''
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3

'''