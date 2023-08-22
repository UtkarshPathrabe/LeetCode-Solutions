class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def numberOfWays(coinIndex: int, remainingAmount: int) -> int:
            if remainingAmount == 0:
                return 1
            if coinIndex == len(coins):
                return 0
            if coins[coinIndex] > remainingAmount:
                return numberOfWays(coinIndex + 1, remainingAmount)
            else:
                return numberOfWays(coinIndex, remainingAmount - coins[coinIndex]) + numberOfWays(coinIndex + 1, remainingAmount)
        return numberOfWays(0, amount)