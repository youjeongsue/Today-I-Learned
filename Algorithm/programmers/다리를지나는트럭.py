from collections import deque

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step

# for i in range(len(truck_weights)+1):
#     if i==len(truck_weights):
#         answer+=bridge_length
#         break
        
#     for j in range(bridge_length):
#         answer+=1
#         if q_sum+truck_weights[i]<=weight:
#             q_sum = q_sum + truck_weights[i] - queue.pop()
#             queue.appendleft(truck_weights[i]) #무게가 남는경우 트럭 추가
            
#             print(queue, q_sum)
#             break
#         else:
#             queue.appendleft(0) #빈칸추가
#             q_sum = q_sum - queue.pop()
#             print(queue, q_sum)