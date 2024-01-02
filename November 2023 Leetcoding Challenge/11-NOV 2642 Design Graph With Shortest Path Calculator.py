class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.n = n
        for fromNode, toNode, cost in edges:
            self.graph[fromNode].append((toNode, cost))

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0, node1)]
        costForNode = [inf] * self.n
        costForNode[node1] = 0
        while pq:
            currentCost, currentNode = heappop(pq)
            if currentCost > costForNode[currentNode]:
                continue
            if currentNode == node2:
                return currentCost
            for neighbour, cost in self.graph[currentNode]:
                newCost = currentCost + cost
                if newCost < costForNode[neighbour]:
                    costForNode[neighbour] = newCost
                    heappush(pq, (newCost, neighbour))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)