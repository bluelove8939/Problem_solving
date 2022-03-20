from queue import Queue
from sys import stdin


graph = list()
isdiscovered = list()


def bfs(start):
    isdiscovered = [False] * len(graph)
    nodequeue = Queue()
    order = list()

    nodequeue.put(start)
    
    while not nodequeue.empty():
        node = nodequeue.get()
        order.append(node)

        for nxt in range(len(graph)):
            if graph[node][nxt] and not isdiscovered[nxt]:
                nodequeue.put(nxt)
                isdiscovered[nxt] = True

    return order


if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        res = 0
        
        print(f"Case #{t}: {res}")