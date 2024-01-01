class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree, graph, queue, maxTime, result = [0] * n, defaultdict(list), deque(), [0] * n, 0
        for x, y in relations:
            graph[x - 1].append(y - 1)
            indegree[y - 1] += 1
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)
                maxTime[node] = time[node]
                result = max(result, maxTime[node])
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                maxTime[neighbour] = max(maxTime[neighbour], maxTime[node] + time[neighbour])
                result = max(result, maxTime[neighbour])
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return result