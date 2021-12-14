N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost, result = cost[0], 0

for i in range(N-1):
    min_cost = min((min_cost, cost[i]))
    result += dist[i] * min_cost

print(result)