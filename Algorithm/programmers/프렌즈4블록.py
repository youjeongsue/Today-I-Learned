from copy import deepcopy

dx, dy = [0, 0, 1, 1], [0, 1, 0, 1] #자신, 하, 우, 대각선

def down(board, m, n):
    new_b=[[0]*n for _ in range(m)]

    for i in range(n):
        #빈칸 제거
        lst = ''.join([str(board[x][i]) for x in range(m)]).replace('0','')
        lst = '0'*(m-len(lst))+lst
        
        for j in range(m):
            new_b[j][i] = lst[j]

    return new_b


def dfs(checked, board, box, i, j):
    checked[i][j]=1
    isbox=1 #i,j에서부터 정사각형이 되는지
    
    for vec in range(1, 4):
        xx, yy = i+dx[vec], j+dy[vec]
        if board[xx][yy]==board[i][j]:
            continue
        isbox=0
        
    if isbox==1: #정사각형이면 box에 네 칸 모두 표시
        for vec in range(4):
            box[i+dx[vec]][j+dy[vec]]=1

#box==1인 원소를 지우고 새로운 board를 리턴하는 함수
def remove(board, box, m, n):
    new_b=[[0]*n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if box[i][j]==1:
                new_b[i][j]=0
            else:
                new_b[i][j]=board[i][j]
    
    return new_b


def solution(m, n, board):
    answer = 0
    
    while True:
        exist=False

        checked=[[0]*n for _ in range(m)]
        r_checked=[[0]*n for _ in range(m)]
        box=[[0]*n for _ in range(m)]

        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]=='0' or checked[i][j]:
                    continue
                dfs(checked, board, box, i, j)

        tmp=sum([sum(lst) for lst in box])
        if tmp>0:
            answer+=tmp
            board=remove(board, box, m, n)
            exist=True

        if not exist:
            break
        board=down(board, m, n)

    return answer


# m=4
# n=5
# board=["CCBDE", "AAADE", "AAABF", "CCBBF"]
# print(solution(m, n, board))