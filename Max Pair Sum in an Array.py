class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def getMaximumDigit(num: int) -> int:
            result, temp = 0, num
            while temp > 0:
                digit = temp % 10
                temp //= 10
                result = max(result, digit)
            return result

        hashMap = defaultdict(list)
        for num in nums:
            maxDigit = getMaximumDigit(num)
            hashMap[maxDigit].append(num)
        result = -1
        for values in hashMap.values():
            for i1, num1 in enumerate(values):
                for i2, num2 in enumerate(values):
                    if i1 == i2:
                        continue
                    result = max(result, num1 + num2)
        return result