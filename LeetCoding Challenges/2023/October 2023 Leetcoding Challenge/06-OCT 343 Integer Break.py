class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dp(num):
            if num <= 3:
                return num
            result = num
            for i in range(2, num):
                result = max(result, i * dp(num - i))
            return result
        if n <= 3:
            return n - 1
        return dp(n)