class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
        vowelList = []
        for char in s:
            if char in VOWELS:
                vowelList.append(char)
        vowelList.sort()
        result, vowelIndex = [], 0
        for char in s:
            if char in VOWELS:
                result.append(vowelList[vowelIndex])
                vowelIndex += 1
            else:
                result.append(char)
        return ''.join(result)