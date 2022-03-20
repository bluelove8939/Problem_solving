class TreeNode:
    def __init__(self, sheep_cnt, wolf_cnt, visited_nodes):
        self.sheep_cnt = sheep_cnt  # the number of sheep
        self.wolf_cnt = wolf_cnt    # the number of wolf
        self.visited_nodes = visited_nodes  # bit-masking set

    def isvisited(self, idx):
        return self.visited_nodes & (1 << idx)


def solution(info, edges):
    graph = [[] for _ in info]
    for a, b in edges: graph[a].append(b)  # adjacent matrix expression of given graph
    visited_set = [False] * pow(2, len(info)+1)  # cache

    # BFS algorithm
    queue = [TreeNode(1, 0, 1)]  # visit node 0
    answer = 1

    while len(queue) != 0:
        nd = queue.pop(0)

        for idx, val in enumerate(info):
            if nd.isvisited(idx):
                for child in graph[idx]:
                    # calculate next state to search
                    sheep_cnt = nd.sheep_cnt
                    wolf_cnt = nd.wolf_cnt
                    visited_nodes = nd.visited_nodes | (1 << child)

                    if not visited_set[visited_nodes]:
                        if info[child] == 0: sheep_cnt += 1
                        elif sheep_cnt > wolf_cnt + 1: wolf_cnt += 1
                        else: continue

                        queue.append(TreeNode(sheep_cnt, wolf_cnt, visited_nodes))
                        answer = max(answer, sheep_cnt)
                        visited_set[visited_nodes] = True

    return answer


if __name__ == '__main__':
    info = [0,1,0,1,1,0,1,0,0,1,0]
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
    print(solution(info, edges))