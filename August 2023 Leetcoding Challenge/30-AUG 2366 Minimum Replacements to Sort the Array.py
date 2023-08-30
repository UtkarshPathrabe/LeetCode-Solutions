class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        result, n = 0, len(nums)
        # Start from the second last element, as the last one is always sorted.
        for i in range(n - 2, -1, -1):
            # No need to break if they are already in order.
            if nums[i] <= nums[i + 1]:
                continue
            # Count how many elements are made from breaking nums[i].
            numElements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
            # It requires numElements - 1 replacement operations.
            result += numElements - 1
            # Maximize nums[i] after replacement.
            nums[i] = nums[i] // numElements
        return result