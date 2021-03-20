def solution(msg):
    answer = []
    num=27
    a_dic = {alpha : num for alpha, num in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', [i for i in range(1,num+1)])}
    left=0
    
    while len(msg)>left:
        right = left+1
        for i in range(1,len(msg)-left):
            if msg[left:left+i+1] in a_dic:
                right=left+i+1
            else:
                break

        answer.append(a_dic[msg[left:right]])
        a_dic[msg[left:right+1]]=num
        num+=1
        
        left = right
            
    return answer

msg='KAKAO'
print(solution(msg))