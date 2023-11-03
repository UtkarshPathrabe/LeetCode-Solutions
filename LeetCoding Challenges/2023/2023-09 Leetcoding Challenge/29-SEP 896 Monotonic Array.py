class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        diff, same = 0, 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                diff += 1
            elif nums[i] > nums[i + 1]:
                diff -= 1
            else:
                same += 1
        return (len(nums) - 1 - same) == abs(diff)