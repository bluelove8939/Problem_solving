class TreeNode:
    def __init__(self, value):
        self.value = value
        self.lnk = []

    def makelink(self, nd):
        if nd not in self.lnk:
            self.lnk.append(nd)


def current_cluster(nd):  # the node 'nd' needs to be a sheep node
    if nd.value == 1:
        return 0

    sheep_nodes, wolf_nodes = [nd], []
    sheep_cnt = 1

    while len(sheep_nodes) != 0:
        nd = sheep_nodes.pop(-1)

        for child in nd.lnk:
            if child.value == 0:
                sheep_nodes.append(child)
                sheep_cnt += 1
            else:
                wolf_nodes.append(child)

    return sheep_cnt, wolf_nodes


def solution(info, edges):
    # Preprocessing inputs
    nodes = [TreeNode(val) for val in info]
    for parent, child in edges:
        nodes[parent].makelink(nodes[child])

    sheep_nodes, wolf_nodes = [], []  # nodes to be visited
    sheep_cnt, wolf_cnt, distance = 0, 0, 0
    sheep_nodes.append(nodes[0])

    # Repeat the overall task until there aren't any node to visit
    while len(sheep_nodes) != 0 or len(wolf_nodes) != 0:
        # Search for current clusters
        while len(sheep_nodes) != 0:
            nd = sheep_nodes.pop(-1)
            tmp_sheep_cnt, tmp_wolf_nodes = current_cluster(nd)
            if sheep_cnt > wolf_cnt+distance:
                sheep_cnt += tmp_sheep_cnt
                wolf_cnt += distance
                wolf_nodes += tmp_wolf_nodes

        # Search for next clusters
        while len(sheep_nodes) == 0 and len(wolf_nodes) != 0:
            distance += 1
            tmp_wolf_nodes = []

            while len(wolf_nodes) != 0:
                nd = wolf_nodes.pop(-1)
                for child in nd.lnk:
                    if child.value == 0: sheep_nodes.append(child)
                    else: tmp_wolf_nodes.append(child)

            wolf_nodes = tmp_wolf_nodes

    answer = sheep_cnt
    return answer


if __name__ == '__main__':
    info = [0,1,0,1,1,0,1,0,0,1,0]
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
    print(solution(info, edges))