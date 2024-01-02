class Solution:
    def countHomogenous(self, s: str) -> int:
        result, currentStreak, MOD = 0, 0, 10 ** 9 + 7
        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                currentStreak += 1
            else:
                currentStreak = 1
            result = (result + currentStreak) % MOD
        return result