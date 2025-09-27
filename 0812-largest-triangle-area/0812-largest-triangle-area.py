class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        area = 0
        for i in range(n-2):
            x1, y1 = points[i][0], points[i][1]
            for j in range(1, n-1):
                x2, y2 = points[j][0], points[j][1]
                for k in range(2, n):
                    x3, y3 = points[k][0], points[k][1]

                    x_min, y_min = min(x1, x2, x3), min(y1, y2, y3)
                    x_max, y_max = max(x1, x2, x3), max(y1, y2, y3)

                    height = y_max - y_min
                    base = x_max - x_min

                    area = max(area, 0.5*base*height)

        return area