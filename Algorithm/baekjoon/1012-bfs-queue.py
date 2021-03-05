'''
bfs 이용
n,m 크기의 배열을 만들어주고(문제에 나온것과 x,y 바꿔서!)
하나씩 검사하면서 배추가 있으면
상하좌우를 검사하는 bfs를 실행(주변에 있으면 1->0으로 바꿔주고, 검사대기큐에 넣어줌)
즉, 한 노드에서 진입하여 상하좌우에 있는 배추를 모두 0으로 만들면 bfs가 끝나고
answer에 1을 더해주며 답을 구한다.
'''

t = int(input())
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue=[[x,y]]
    while queue:
        _x, _y = queue[0][0], queue[0][1]
        del queue[0] #현재 위치

        for i in range(4): #상하좌우
            xx, yy = _x+dx[i], _y+dy[i] #다음 좌표
            #inputs[xx][yy]==1 부분이 다음 좌표로 가는 조건 검사 부분 ← 문제에 따라 적절히!
            if 0<=xx<n and 0<=yy<m and inputs[xx][yy]==1:
                inputs[xx][yy]=0
                queue.append([xx, yy])

for _ in range(t):
    m, n, k = map(int, input().split())
    inputs = [[0]*m for _ in range(n)]
    answer = 0

    for _ in range(k):
        x, y = map(int, input().split())
        inputs[y][x]=1

    for x in range(n):
        for y in range(m):
            if inputs[x][y]==1:
                bfs(x,y)
                inputs[x][y]=0
                answer+=1
    print(answer)