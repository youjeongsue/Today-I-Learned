from copy import deepcopy

#90도 회전하는 함수
def rotate(n, b):
    nb = deepcopy(b)
    for i in range(n):
        for j in range(n):
            nb[j][n-i-1] = b[i][j]
    return nb

# 2 2 2 0 2
# 2 2 2 2 0 -> 사이에 있는 0 빼기
# 4 0 4 0 0 -> 옆에 같은 숫자면 합치기
# 4 4 0 0 0 -> 사이 0 빼기
def convert(lst, n):
    new_lst = [i for i in lst if i]
    for i in range(1, len(new_lst)):
        if new_lst[i-1] == new_lst[i]:
            new_lst[i-1] *= 2
            new_lst[i] = 0
    new_lst = [i for i in new_lst if i]
    return new_lst + [0]*(n-len(new_lst))

def dfs(n, b, count):
    answer = max([max(lst) for lst in b])
    if count == 0:
        return answer
    for _ in range(4):
        converted = [convert(lst, n) for lst in b]
        if converted != b:
            answer = max(answer, dfs(n, converted, count-1)) #★
        
        b = rotate(n, b)

    return answer


n = int(input())
board = [list(map(int, input().split())) for i in range(n)]

print(dfs(n, board, 5))