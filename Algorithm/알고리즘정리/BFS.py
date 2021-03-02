from collections import deque

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    
    return visited

graph = []
root=0

print(BFS(graph, root))