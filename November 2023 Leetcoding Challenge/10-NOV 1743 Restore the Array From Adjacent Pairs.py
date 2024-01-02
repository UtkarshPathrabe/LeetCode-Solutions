class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for node1, node2 in adjacentPairs:
            graph[node1].append(node2)
            graph[node2].append(node1)
        start = None
        for key, value in graph.items():
            if len(value) == 1:
                root = key
                break
        result = []
        def dfs(node, prev):
            result.append(node)
            for neighbour in graph[node]:
                if neighbour != prev:
                    dfs(neighbour, node)
        dfs(root, None)
        return result