from sys import stdin


graph = list()
isvisited = list()


def dfs(node):
    isvisited[node] = True

    for nxt in range(len(graph)):
        if graph[node][nxt] and not isvisited[nxt]:
            dfs(nxt)
    

def dfsAll():
    isvisited = [False] * len(graph)

    for node in range(len(graph)):
        if not isvisited[node]:
            dfs(node)


if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        res = 0
        
        print(f"Case #{t}: {res}")