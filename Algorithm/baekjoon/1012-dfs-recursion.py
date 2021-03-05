import sys
sys.setrecursionlimit(10000) #recursion 한계를 정해줘야함

T = int(input())
inputs, checked= [], []
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

#dfs-재귀버전
def dfs(x, y):
    checked[x][y]=1 #방문하면 체크
    for i in range(4):
        #xx, yy: 다음에 방문할 지점
        xx, yy = x + dx[i], y + dy[i]
        if inputs[xx][yy]==0 or checked[xx][yy]==1:
            continue
        dfs(xx, yy)

for _ in range(T):
    M, N, K = map(int, input().split())

    # dfs/bfs에서 상하좌우를 만들때, 예외를 만들지 않기 위해 두칸씩 늘려서 만든다.   
    # 이렇게 안하는 경우 dfs 안에서 검사해야함
    inputs = [[0]*(M+2) for j in range(N+2)]
    checked = [[0]*(M+2) for j in range(N+2)]

    for k in range(K):
        x, y = map(int, input().split())
        inputs[y+1][x+1]=1 #가로세로 스왑

    answer=0
    for x in range(1, N+1):
        for y in range(1, M+1):
            #배추가 있고 방문하지 않은 경우 dfs
            if inputs[x][y]==0 or checked[x][y]==1:
                continue
            dfs(x, y)
            answer+=1
    print(answer)