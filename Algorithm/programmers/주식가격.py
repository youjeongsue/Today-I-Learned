def solution(prices):
    answer = []
    len_prices = len(prices)
    
    for i in range(len_prices-1):
        sub_answer=0
        for j in range(i+1, len_prices):
            sub_answer+=1
            if prices[j] < prices[i]:
                break
        answer.append(sub_answer)
    answer.append(0)
    
    return answer