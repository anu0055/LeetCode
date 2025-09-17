import java.util.*;

class Solution {
    private int dfs(int[][] grid, int r, int c, int id) {
        int m = grid.length, n = grid[0].length;
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != 1) return 0;

        grid[r][c] = id; // mark with island id
        int area = 1;

        // explore 4 directions
        area += dfs(grid, r + 1, c, id);
        area += dfs(grid, r - 1, c, id);
        area += dfs(grid, r, c + 1, id);
        area += dfs(grid, r, c - 1, id);

        return area;
    }

    public int largestIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Map<Integer, Integer> areaMap = new HashMap<>(); // id -> area
        int id = 2; // start marking islands from 2
        int maxArea = 0;

        // 1️⃣ Mark each island with unique id & record area
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    int area = dfs(grid, i, j, id);
                    areaMap.put(id, area);
                    maxArea = Math.max(maxArea, area);
                    id++;
                }
            }
        }

        // 2️⃣ Try flipping each 0 → check connected unique islands
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    Set<Integer> seen = new HashSet<>();
                    int newArea = 1; // flip current 0 → 1

                    int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
                    for (int[] d : dirs) {
                        int nr = i + d[0], nc = j + d[1];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                            int neighborId = grid[nr][nc];
                            if (neighborId > 1 && seen.add(neighborId)) {
                                newArea += areaMap.get(neighborId);
                            }
                        }
                    }
                    maxArea = Math.max(maxArea, newArea);
                }
            }
        }

        // 3️⃣ Edge case: all 1s
        return maxArea == 0 ? m * n : maxArea;
    }
}
