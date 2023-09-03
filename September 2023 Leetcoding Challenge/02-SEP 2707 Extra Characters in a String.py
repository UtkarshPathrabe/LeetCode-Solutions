class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionarySet = set(dictionary)
        @lru_cache(None)
        def dp(start):
            if start == len(s):
                return 0
            # To count this character as a left over character 
            # move to index 'start + 1'
            result = dp(start + 1) + 1
            for end in range(start, len(s)):
                word = s[start: end + 1]
                if word in dictionarySet:
                    result = min(result, dp(end + 1))
            return result
        return dp(0)