class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        hashSet = set()
        for startRange, endRange in nums:
            hashSet |= set(range(startRange, endRange + 1))
        return len(hashSet)