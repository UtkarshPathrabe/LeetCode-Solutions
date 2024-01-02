class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxElement, current, winStreak = max(arr), arr[0], 0
        for i in range(1, len(arr)):
            opponent = arr[i]
            if current > opponent:
                winStreak += 1
            else:
                current = opponent
                winStreak = 1
            if winStreak == k or current == maxElement:
                return current