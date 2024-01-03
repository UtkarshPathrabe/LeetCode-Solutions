class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result, prevLaserCount = 0, 0
        for lasers in bank:
            laserCount = lasers.count('1')
            if laserCount > 0:
                result += laserCount * prevLaserCount
                prevLaserCount = laserCount
        return result