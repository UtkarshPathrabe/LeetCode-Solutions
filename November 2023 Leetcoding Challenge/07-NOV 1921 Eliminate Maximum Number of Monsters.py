class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrivals = [d/s for d, s in zip(dist, speed)]
        arrivals.sort()
        result = 0
        for i, arr in enumerate(arrivals):
            if arr <= i:
                break
            result += 1
        return result