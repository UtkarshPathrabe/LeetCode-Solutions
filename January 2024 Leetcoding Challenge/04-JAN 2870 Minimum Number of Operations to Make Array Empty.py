class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freqMap = Counter(nums)
        result = 0
        for value in freqMap.values():
            if value == 1:
                return -1
            result += ceil(value / 3)
        return result