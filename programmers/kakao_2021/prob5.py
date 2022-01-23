class BinTreeNode:
    def __init__(self, value=0):
        self.value = 0
        self.distance = 0
        self.parent_sheep = None
        self.lnk = []


    def nodeinit(self, parent_sheep=None, distance=0):
        self.parent_sheep = parent_sheep
        self.distance = distance
        for nd in self.lnk:
            if self.value == 0: nd.nodeinit(self, 0)
            else: nd.nodeinit(parent_sheep, distance+1)


    def dfs(self, sheep, wolf):
        pass


def solution(info, edges):
    nodes = [BinTreeNode(value=val) for val in info]
    for ed in edges: nodes[ed[0]].lnk.append(nodes[ed[1]])
    answer = nodes[0].dfs(sheep=0, wolf=0)
    return answer


if __name__ == '__main__':
    info = [0,0,1,1,1,0,1,0,1,0,1,1]
    edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
    print(solution(info, edges))