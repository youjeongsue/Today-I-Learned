T=int(input())

def solve(M, N, K, inputs):
    pass

for i in range(T):
    M, N, K = map(int, input().split())
    inputs = [[0 for i in range(M)] for j in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        inputs[x][y]=1
    
    solve(M, N, K, inputs)