n, m = map(int, input().split())
inputs = [[0]*m for _ in range(n)]
dp = [[0]*m for _ in range(n)]

for i in range(n):
    tmp = input()
    inputs[i] = [int(tmp[j]) for j in range(m)]

mx = 0

for i in range(n):
    for j in range(m):
        if inputs[i][j]:
            dp[i][j]=min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            mx = max(dp[i][j], mx)
        

print(mx*mx)

'''
4 4
0100
0111
1110
0010

'''