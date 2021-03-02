N, B = int(input()), list(map(int, input().split()))
A = []

for i in range(N):
    A.append(B[i]*(i+1)-sum(A[:i]))
    
# 이 문제에서는 이렇게 안하고 그냥 sum(A)해도됨
# N이 클때는 미리 최대 개수만큼 선언해두고
# 리스트를 수정하는게 빠를 수도 있다.

print(*A)