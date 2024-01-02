class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Array to store the prefix sum in travel.
        prefixSum = [0] * (len(travel) + 1)
        prefixSum[1] = travel[0]
        for i in range(1, len(travel)):
            prefixSum[i + 1] = prefixSum[i] + travel[i]
        # Map to store garbage type to the last house index.
        garbageLastPosition = defaultdict(int)
        # Map to store the total count of each type of garbage in all houses.
        garbageCount = defaultdict(int)
        for i in range(len(garbage)):
            for char in garbage[i]:
                garbageLastPosition[char] = i
                garbageCount[char] += 1
        result, garbageTypes = 0, ['M', 'P', 'G']
        for garbageType in garbageTypes:
            if garbageType in garbageCount:
                result += prefixSum[garbageLastPosition[garbageType]] + garbageCount[garbageType]
        return result