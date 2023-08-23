class Solution:
    def reorganizeString(self, s: str) -> str:
        charFreqMap = Counter(s)
        maxFreq, maxFreqChar = 0, ''
        for char, count in charFreqMap.items():
            if count > maxFreq:
                maxFreq = count
                maxFreqChar = char
        if maxFreq > (len(s) + 1) // 2:
            return ''
        ans = [''] * len(s)
        index = 0

        # Place the most frequent letter
        while charFreqMap[maxFreqChar] != 0:
            ans[index] = maxFreqChar
            index += 2
            charFreqMap[maxFreqChar] -= 1

        # Place rest of the letters in any order
        for char, count in charFreqMap.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                ans[index] = char
                index += 2
                count -= 1

        return ''.join(ans)