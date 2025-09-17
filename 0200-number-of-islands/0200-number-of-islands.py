class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = 0

        def dfs(i, j, grid, visited):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0' or visited[i][j] == True:
                return
            visited[i][j] = True
            dfs(i-1, j, grid, visited) # UP
            dfs(i, j+1, grid, visited) # RIGHT
            dfs(i+1, j, grid, visited) # DOWN
            dfs(i, j-1, grid, visited) # LEFT

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == False:
                    dfs(i, j, grid, visited)
                    res += 1
        return res