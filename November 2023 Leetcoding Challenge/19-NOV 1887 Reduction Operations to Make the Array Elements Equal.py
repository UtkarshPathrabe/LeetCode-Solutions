class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freqMap = Counter(nums)
        distinctNums = sorted(set(nums))
        result = 0
        for i, num in enumerate(distinctNums[1:], start=1):
            result += i * freqMap[num]
        return result