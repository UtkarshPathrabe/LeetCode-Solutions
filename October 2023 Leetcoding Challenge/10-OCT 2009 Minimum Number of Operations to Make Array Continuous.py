class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        result, j = n, 0
        sortedNums = sorted(set(nums))
        for i in range(len(sortedNums)):
            while j < len(sortedNums) and sortedNums[j] < sortedNums[i] + n:
                j += 1
            count = j - i
            result = min(result, n - count)
        return result