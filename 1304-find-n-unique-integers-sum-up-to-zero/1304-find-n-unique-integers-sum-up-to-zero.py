class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0]*n
        if n == 1:
            return res
        if n%2 != 0:
            l = n//2 - 1
            r = n//2 + 1
            i = 1 
            while l >= 0 and r < n:
                res[l] = -i
                res[r] = i
                i += 1
                l -= 1
                r += 1
        else:
            l = n//2-1
            r = n//2
            i = 1
            while l >= 0 and r < n:
                res[l] = -i
                res[r] = i
                i += 1
                l -= 1
                r += 1
        return res