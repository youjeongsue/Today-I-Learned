def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    print(routes)
    
    st = ['ICN']
    ans = []
    while st:
        top = st[-1]
        if top not in routes or len(routes[top])==0:
            ans.append(st.pop())
        else:
            st.append(routes[top].pop())
    ans.reverse()
    return ans

tickets=[['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
print(solution(tickets))