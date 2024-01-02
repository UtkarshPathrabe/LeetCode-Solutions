class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        for i in range(len(nums)):
            current = nums[i][i]
            result.append('1' if current == '0' else '0')
        return ''.join(result)