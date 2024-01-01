class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @lru_cache(None)
        def dp(i, remain):
            if remain <= 0:
                return 0
            if i == len(cost):
                return inf
            paint = cost[i] + dp(i + 1, remain - 1 - time[i])
            dontPaint = dp(i + 1, remain)
            return min(paint, dontPaint)
        return dp(0, len(cost))