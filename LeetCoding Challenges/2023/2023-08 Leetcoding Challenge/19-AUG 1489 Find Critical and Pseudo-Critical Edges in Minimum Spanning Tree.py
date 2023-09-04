class UnionFind:
    def __init__(self, n):
        self._parent = list(range(n))
        self._size = [1] * n
        self.maxSize = 1
    
    # Finds the root of x
    def find(self, x):
        if x != self._parent[x]:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    # Connects x and y
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self._size[rootX] < self._size[rootY]:
                rootX, rootY = rootY, rootX
            self._parent[rootY] = rootX
            self._size[rootX] += self._size[rootY]
            self.maxSize = max(self.maxSize, self._size[rootX])
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        newEdges = [(edge[0], edge[1], edge[2], index) for index, edge in enumerate(edges)]
        newEdges.sort(key = lambda x:x[2])
        # Find Minimum Spanning Tree
        mstWeight, uf = 0, UnionFind(n)
        for u, v, w, _ in newEdges:
            if uf.union(u, v):
                mstWeight += w
        # Check each edge for critical and pseudo-critical
        critical, pseudoCritical = [], []
        for u, v, w, i in newEdges:
            # Ignore this edge and calculate MST weight
            weightIgnore, ufIgnore = 0, UnionFind(n)
            for x, y, wIgnore, j in newEdges:
                if i != j and ufIgnore.union(x, y):
                    weightIgnore += wIgnore
            # If the graph is disconnected or the total weight is greater,
            # the edge is critical
            if ufIgnore.maxSize < n or weightIgnore > mstWeight:
                critical.append(i)
                continue
            # Force this edge and calculate MST weight
            weightForce, ufForce = w, UnionFind(n)
            ufForce.union(u, v)
            for x, y, wForce, j in newEdges:
                if i != j and ufForce.union(x, y):
                    weightForce += wForce
            # If total weight is the same, the edge is pseudo-critical
            if weightForce == mstWeight:
                pseudoCritical.append(i)
        return [critical, pseudoCritical]