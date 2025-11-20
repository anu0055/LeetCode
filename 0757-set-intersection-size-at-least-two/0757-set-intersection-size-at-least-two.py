from typing import List
import bisect

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end ascending (and start descending is common, but start asc also works here)
        intervals.sort(key=lambda x: (x[1], -x[0]))

        chosen = []   # sorted list of chosen points
        in_set = set()  # membership check

        for s, e in intervals:
            # count how many chosen points are inside [s, e]
            left = bisect.bisect_left(chosen, s)
            cnt = 0
            idx = left
            while idx < len(chosen) and chosen[idx] <= e:
                cnt += 1
                idx += 1

            need = 2 - cnt
            x = e
            # add the required number of points starting from the right (e, e-1, ...)
            while need > 0:
                if x not in in_set:
                    bisect.insort(chosen, x)
                    in_set.add(x)
                    need -= 1
                x -= 1

        return len(chosen)
