class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        for point1 in points:
            for point2 in points:
                if point1 == point2:
                    continue
                set_ = {(point1[0], point1[1]), (point2[0], point2[1])}
                if point1[0] <= point2[0] and point1[1] >= point2[1]:
                    valid = True
                    for points_in_between in points:
                        if (points_in_between[0], points_in_between[1]) in set_:
                            continue
                        if point1[0] <= points_in_between[0] <= point2[0] and point2[1] <= points_in_between[1] <= point1[1]:
                            valid = False
                            break
                    if valid:
                        ans += 1
        return ans
