class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            currentResult = nums1[i] * nums2[j] + dp(i + 1, j + 1)
            return max(currentResult, dp(i + 1, j), dp(i, j + 1))
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        return dp(0, 0)