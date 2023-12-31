class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def trimmedString(s):
            skip = 0
            for x in s[::-1]:
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
        return all(x == y for x, y in zip_longest(trimmedString(S), trimmedString(T)))