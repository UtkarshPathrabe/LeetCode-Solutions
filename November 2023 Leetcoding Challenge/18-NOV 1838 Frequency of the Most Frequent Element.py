class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, result, currentSum = 0, 0, 0
        for right in range(len(nums)):
            target = nums[right]
            currentSum += target
            while ((right - left + 1) * target) - currentSum > k:
                currentSum -= nums[left]
                left += 1
            result = max(result, right - left + 1)
        return result