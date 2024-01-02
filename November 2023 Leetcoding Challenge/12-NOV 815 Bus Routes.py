class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(list)
        # Create a map from the bus stop to all the routes that include this stop.
        for r in range(len(routes)):
            for stop in routes[r]:
                # Add all the routes that have this stop.
                route = graph[stop]
                route.append(r)
                graph[stop] = route
        queue = deque()
        visited = set()
        # Insert all the routes in the queue that have the source stop.
        for route in graph[source]:
            queue.append(route)
            visited.add(route)
        busCount = 1
        while len(queue) != 0:
            size = len(queue)
            for i in range(size):
                route = queue.popleft()
                # Iterate over the stops in the current route.
                for stop in routes[route]:
                    # Return the current count if the target is found.
                    if stop == target:
                        return busCount
                    # Iterate over the next possible routes from the current stop.
                    for nextRoute in graph[stop]:
                        if nextRoute not in visited:
                            visited.add(nextRoute)
                            queue.append(nextRoute)
            busCount += 1
        return -1