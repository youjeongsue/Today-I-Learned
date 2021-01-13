def solution(progresses, speeds):
    answer = []
    days = [100]*len(progresses)
    
    for i in range(len(days)):
        if (days[i]-progresses[i]) % speeds[i] == 0:
            days[i] = (days[i]-progresses[i]) // speeds[i]
        else:
            days[i] = (days[i]-progresses[i]) // speeds[i] +1
        
    sub_answer=1
    day=days[0]
    
    for i in range(1, len(days)):
        if day < days[i]:
            answer.append(sub_answer)
            sub_answer=1
            day=days[i]
        else:
            sub_answer+=1
    
    answer.append(sub_answer)
    
    return answer