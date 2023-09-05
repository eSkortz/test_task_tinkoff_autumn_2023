def create_graph(n: int, roads: int, length_limit: int = 0) -> list:
    graph = [[] for _ in range(n)]
    for road in roads:
        u, v, w = map(int, road.split())
        if w > length_limit:
            graph[u - 1].append((v - 1, w))
            graph[v - 1].append((u - 1, w))
    return graph

def find_states(graph: list) -> int:
    n = len(graph)
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor[0]]:
                dfs(neighbor[0])
    
    state_count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            state_count += 1
    
    return state_count

n, m = map(int, input().split())
roads = [input() for _ in range(m)]

graph = create_graph(n, roads)

state_count = find_states(graph)

x = 1

while True:
    new_graph = create_graph(n, roads, length_limit=x)
    new_state_count = find_states(new_graph)
    
    if new_state_count != state_count:
        break
    else:
        x += 1
        
print(x-1)