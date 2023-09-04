class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)

        @lru_cache(None)
        def solve(stone, k):
            if stone in stones_set:
                # Current stone is equal to last stone
                if stone == stones[-1]:
                    return True
                # Have max(k-1, 1) to avoid infinite loops
                for next_leap in range(max(k-1, 1), k+2):
                    if solve(stone+next_leap, next_leap):
                        return True
            return False

        return solve(0, 0)