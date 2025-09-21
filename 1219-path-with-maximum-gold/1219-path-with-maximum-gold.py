class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_gold = 0
        visited = [[False for _ in range(n)] for _ in range(m)]

        def findMaxGold(r, c, grid, visited):
            if (r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or visited[r][c]):
                return 0
            visited[r][c] = True
            left = findMaxGold(r, c-1, grid, visited)
            up = findMaxGold(r-1, c, grid, visited)
            right = findMaxGold(r, c+1, grid, visited)
            down = findMaxGold(r+1, c, grid, visited)
            visited[r][c] = False

            return max(left, up, right, down) + grid[r][c]

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    gold = findMaxGold(i, j, grid, visited)
                    max_gold = max(max_gold, gold)
        
        return max_gold