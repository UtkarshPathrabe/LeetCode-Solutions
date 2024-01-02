class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum, N = 0, len(nums)
        for i in range(N // 2):
            maxSum = max(maxSum, nums[i] + nums[N - 1 - i])
        return maxSum