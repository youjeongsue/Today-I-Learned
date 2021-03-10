from copy import deepcopy

n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
Q = [tuple(map(int, input().split())) for _ in range(k)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] #남서북동
answer = 10000

def value(lst):
    return min([sum(i) for i in lst])

#어려운 구현 문제
def convert(lst, qry):
    r, c, s = qry
    r, c = r-1, c-1
    new_lst = deepcopy(lst)

    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for j in range(4): #방향
            for k in range(i*2): #방향 당 개수
                rrr, ccc = rr+dx[j], cc+dy[j]
                new_lst[rrr][ccc] = lst[rr][cc]
                rr, cc = rrr, ccc
    return new_lst


def dfs(lst, qry):
    global answer
    if sum(qry) == k:
        answer = min(answer, value(lst))
        return

    for i in range(k):
        if qry[i]:
            continue
        new_lst = convert(lst, Q[i])
        qry[i]=1
        dfs(new_lst, qry)
        qry[i]=0

dfs(data, [0]*k)
print(answer)

#50*50*6*720