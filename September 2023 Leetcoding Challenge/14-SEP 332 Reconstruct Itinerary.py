class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flightGraph, itinerary = defaultdict(list), []
        # Populate the flight graph using ticket information
        for fromAirport, toAirport in tickets:
            flightGraph[fromAirport].append(toAirport)
        # Sort destinations in reverse order to visit lexical smaller destinations first
        for destinations in flightGraph.values():
            destinations.sort(reverse = True)
        # Depth-First Search to traverse the flight itinerary
        def dfs(airport: string):
            destinations = flightGraph[airport]
            # Visit destinations in lexical order
            while destinations:
                dfs(destinations.pop())
            # Add the current airport to the itinerary after visiting all destinations
            itinerary.append(airport)
        # Start the DFS from the JFK airport
        dfs('JFK')
        # Reverse the itinerary to get the correct order
        itinerary.reverse()
        return itinerary