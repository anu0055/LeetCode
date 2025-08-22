class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        temp = [0]*c
        min_row, max_row = 1001, -1
        for COL in range(c):
            curr = 0
            for ROW in range(r):
                curr |= grid[ROW][COL]
                if grid[ROW][COL] == 1:
                    min_row = min(min_row, ROW)
                    max_row = max(max_row, ROW)
            temp[COL] = curr
        min_col, max_col = 1001, -1
        for i in range(len(temp)):
            if temp[i] == 1:
                min_col = min(min_col, i)
                max_col = max(max_col, i)
        
        return (max_col-min_col+1) * (max_row-min_row+1)
        # max_row = -1
        # max_col = -1
        # for i in range(r):
        #     for j in range(c):
        #         if grid[i][j] == 1:
        #             max_row = max(max_row, i)
        #             max_col = max(max_col, j)
        # print(max_row, max_col)
        # return (max_row+1)*(max_col+1)