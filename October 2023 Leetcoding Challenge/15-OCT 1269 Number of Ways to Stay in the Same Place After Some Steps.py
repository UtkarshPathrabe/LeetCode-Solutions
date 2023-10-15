class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        @lru_cache(None)
        def dp(current, remain):
            if remain == 0:
                if current == 0:
                    return 1
                return 0
            result = dp(current, remain - 1)
            if current > 0:
                result = (result + dp(current - 1, remain - 1)) % MOD
            if current < arrLen - 1:
                result = (result + dp(current + 1, remain - 1)) % MOD
            return result
        return dp(0, steps)