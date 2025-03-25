class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        # Check if valid cuts can be made in a specific dimension
        def _check_cuts(rectangles: list[list[int]], dim: int) -> bool:
            gap_count = 0

            # Sort rectangles by their starting coordinate in the given dimension
            rectangles.sort(key=lambda rect: rect[dim])

            # Track the furthest ending coordinate seen so far
            furthest_end = rectangles[0][dim + 2]

            for i in range(1, len(rectangles)):
                rect = rectangles[i]

                # If current rectangle starts after the furthest end we've seen,
                # we found a gap where a cut can be made
                if furthest_end <= rect[dim]:
                    gap_count += 1

                # Update the furthest ending coordinate
                furthest_end = max(furthest_end, rect[dim + 2])

            # We need at least 2 gaps to create 3 sections
            return gap_count >= 2

        # Try both horizontal and vertical cuts
        return _check_cuts(rectangles, 0) or _check_cuts(rectangles, 1)
    # def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
    #     def canCutVertically(n, rectangles):
    #         rectangles.sort(key = lambda x : x[2])
    #         i = 0
    #         verticle_cuts = 0
    #         while i < n-1:
    #             if rectangles[i][2] <= rectangles[i+1][2]:
    #                 if rectangles[i][2] == rectangles[i+1][0]:
    #                     verticle_cuts += 1
    #                     i += 1
    #                 else:
    #                     i += 1 
    #         return verticle_cuts == 2

    #     def canCutHorizontally(n, rectangles):
    #         rectangles.sort(key = lambda x : x[3])
    #         i = 0
    #         horizontal_cuts = 0
    #         while i < n-1:
    #             if rectangles[i][3] <= rectangles[i+1][3]:
    #                 if rectangles[i][3] == rectangles[i+1][1]:
    #                     horizontal_cuts += 1
    #                     i += 1
    #                 else:
    #                     i += 1
    #         return horizontal_cuts == 2
        
    #     return canCutHorizontally(n, rectangles) or canCutVertically(n, rectangles)