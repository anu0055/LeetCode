class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9+7
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == "1":
                j = i
                while j < len(s) and s[j] == "1":
                    j += 1
                n = (j - i)%mod
                ans += (n*(n+1)//2)%mod
                i = j - 1
            i += 1
        return ans%mod
            