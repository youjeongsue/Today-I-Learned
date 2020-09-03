T = int(input())
for _ in range(T):
    dp = []
    n = int(input())

    for _ in range(2):
        dp.append(list(map(int, input().split())))
    
    #col1의 값을 미리 계산해둠
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    
    #남은 값들을 계산함
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
        
    print(max(dp[0][n-1], dp[1][n-1]))