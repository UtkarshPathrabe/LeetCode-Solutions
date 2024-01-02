class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        result = 0
        for num in left:
            result = max(num, result)
        for num in right:
            result = max(n - num, result)
        return result