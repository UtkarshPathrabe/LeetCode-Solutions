class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freqMap = Counter(nums)
        result = []
        keySet = set(freqMap)
        while len(keySet) > 0:
            temp = []
            for key in keySet:
                temp.append(key)
                freqMap[key] -= 1
                if freqMap[key] == 0:
                    del freqMap[key]
            result.append(temp)
            keySet = set(freqMap)
        return result