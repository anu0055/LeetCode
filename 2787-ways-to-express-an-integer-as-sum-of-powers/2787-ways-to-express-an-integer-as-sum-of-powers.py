class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 1000000007

        @lru_cache(None)
        def dp(num, k):
            take = 0
            not_take = 0
            if num == 0:
                return 1
            if num < 0 or k**x > num:
                return 0
            take += dp(num-(k**x), k+1)%mod
            not_take += dp(num, k+1)%mod
            return (take + not_take)%mod

        return dp(n, 1)