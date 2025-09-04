class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff_1 = abs(z-x)
        diff_2 = abs(z-y)
        if diff_1 < diff_2:
            return 1
        elif diff_1 > diff_2:
            return 2
        else:
            return 0