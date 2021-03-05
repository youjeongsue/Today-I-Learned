import sys
sys.setrecursionlimit(10000)

n, k = map(int, input().split())
inputs=[list(input()) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

def reset_checked():
    return [[0]*10 for _ in range(n)]

def dfs(x, y):
    checked[x][y]=1
    count=1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        #상하좌우 값이 현재 비교값과 같으면 더 진행
        if 0<=xx<n and 0<=yy<10 and inputs[xx][yy]==inputs[x][y] and checked[xx][yy]==0:
            count += dfs(xx, yy) #상하좌우로 진행해서 합함
    return count

def dfs_remove(x, y, value):
    checked2[x][y]=1
    inputs[x][y]='0'
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        #상하좌우 값이 현재 비교값과 같으면 더 진행, 0으로 변경
        if 0<=xx<n and 0<=yy<10 and inputs[xx][yy]==value and checked2[xx][yy]==0:
            dfs_remove(xx, yy, value)

def down():
    for x in range(10):
        tmp=[]
        for y in range(n):
            if inputs[y][x]!='0':
                tmp.append(inputs[y][x])
        
        downed=['0']*(n-len(tmp))+tmp
        for y in range(n):
            inputs[y][x]=downed[y]


while True:
    exist=False
    
    checked=reset_checked() #dfs용 checked
    checked2=reset_checked() #dfs_remove용 checked
    for x in range(n):
        for y in range(10):
            if inputs[x][y]=='0' or checked[x][y]:
                continue
            count = dfs(x,y) #(x,y)와 같은 원소 개수 구하기
            # print(inputs[x][y], 'count > ', count)
            if count >= k:
                dfs_remove(x,y, inputs[x][y])
                exist=True

    if not exist: #더 이상 없을 때
        break
    down() #내리기

for line in inputs:
    print(''.join(line))