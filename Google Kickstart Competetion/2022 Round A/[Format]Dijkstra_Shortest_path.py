from sys import stdin
from queue import PriorityQueue
import math


INF = math.inf
V = 0   # the number of nodes
graph = list()   # adjacent list


def dijkstra(src):
    dist = [INF] * V
    dist[src] = 0
    pq = PriorityQueue()
    pq.put((0, src))

    while not pq.empty():
        cost, node = pq.get()

        if dist[node] < cost:
            continue
            
        for nxt, weight in graph[node]:
            nxt_dist = cost + weight

            if dist[nxt] > nxt_dist:
                dist[nxt] = nxt_dist
                pq.put((nxt_dist, nxt))

    return dist


if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        res = 0
        
        print(f"Case #{t}: {res}")