from copy import deepcopy

n = int(input())
inputs = list(map(int, input().split()))
dp = deepcopy(inputs)
lst = [i for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if inputs[i] > inputs[j] and inputs[i]+dp[j] > dp[i]:
            dp[i] = inputs[i]+dp[j]
            lst[i] = j

print('최대값: ', max(dp))

answer = [inputs[dp.index(max(dp))]]
now=0
idx=dp.index(max(dp))
while True:
    idx=lst[idx]
    if idx==now:
        print('부분수열: ', answer[::-1])
        break
    now=idx
    answer.append(inputs[idx])