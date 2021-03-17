#u, v로 나누는 함수
def divide(string):
    idx=0
    cnt1, cnt2=0,0
    for s in string:
        idx+=1
        if s=='(': cnt1+=1
        else: cnt2+=1
        if cnt1==cnt2:
            return string[:idx], string[idx:]

#올바른 문자열인지 확인하는 함수
def check(string):
    closed=0
    for s in string:
        if s==')': closed-=1
        else: closed+=1
        
        if closed<0:
            return False
    return True

def solution(p):
    answer = ''
    
    #1단계
    if p=='':
        return ''
    if check(p):
        return p
    
    #2단계
    u, v = divide(p)
    
    #3단계
    if check(u):
        return u + solution(v)
    
    #4단계
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        #5단계
        for i in u[1: len(u)-1]:
            if i=='(':
                answer+=')'
            else:
                answer+='('
        return answer