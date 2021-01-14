#feedback: binary queue를 따로 만들어서 썼는데
#priorities를 index랑 같이 zip으로 묶고 location으로 검사하면 됨!

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    binary_queue = deque([1 if i==location else 0 for i in range(len(priorities))])
    max_q = max(queue)
    
    while queue:
        pop = queue.popleft()
        b_pop = binary_queue.popleft()
        
        if pop < max_q:
            queue.append(pop)  #더 큰 작업이 있을때 뒤로 옮김
            binary_queue.append(b_pop)
        else:
            answer+=1
            if b_pop == 1:
                break
            max_q = max(queue)
        
    return answer