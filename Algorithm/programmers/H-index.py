def solution(citations):
    h=max(citations)
    while h:
        answer=sum(1 for x in citations if x>=h)
        if answer >= h:
           break
        h-=1
    return h