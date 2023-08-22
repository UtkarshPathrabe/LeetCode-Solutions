class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def isValidPrefix(i: int) -> bool:
            if i == -1:
                return True
            result = False
            if i > 0 and nums[i] == nums[i - 1]:
                result |= isValidPrefix(i - 2)
            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                result |= isValidPrefix(i - 3)
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                result |= isValidPrefix(i - 3)
            return result
        return isValidPrefix(len(nums) - 1)