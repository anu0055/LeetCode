from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        # dp[r][c][s] = number of ways from (r,c) to end when current sum modulo k is s
        dp = [[[-1] * k for _ in range(n)] for _ in range(m)]

        def solve(r: int, c: int, curr_sum: int) -> int:
            # curr_sum is already mod k
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0

            new_sum = (curr_sum + grid[r][c]) % k

            # If we're at the bottom-right cell, check if sum % k == 0
            if r == m - 1 and c == n - 1:
                return 1 if new_sum == 0 else 0

            if dp[r][c][curr_sum] != -1:
                return dp[r][c][curr_sum]

            right = solve(r, c + 1, new_sum)
            down = solve(r + 1, c, new_sum)

            dp[r][c][curr_sum] = (right + down) % mod
            return dp[r][c][curr_sum]

        return solve(0, 0, 0)
