class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_strt = 0
        window_end = 0
        n = len(s)
        Map = {}
        max_len = float('-inf')

        while(window_end<n):
            ch = s[window_end]
            if(ch in Map and Map[ch]>=window_strt):

                window_strt = Map[ch] + 1
            Map[ch] = window_end
            max_len = max(max_len, window_end-window_strt+1)
            window_end += 1
        return 0 if max_len==float('-inf') else max_len