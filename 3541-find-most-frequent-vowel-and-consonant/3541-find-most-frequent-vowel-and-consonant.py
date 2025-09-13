class Solution:
    def maxFreqSum(self, s: str) -> int:
        vw_cnt = 0
        con_cnt = 0
        freq = [0]*26
        for c in s:
            freq[ord(c) - ord('a')] += 1
            if c in 'aeiou':
                vw_cnt = max(vw_cnt, freq[ord(c)-ord('a')])
            else:
                con_cnt = max(con_cnt, freq[ord(c)-ord('a')])
        return vw_cnt+con_cnt