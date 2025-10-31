class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)
        longest = 0
        for num in set_:
            count = 0
            if num - 1 not in set_:
                while num in set_:
                    count += 1
                    num += 1
                longest = max(longest, count)
        return longest
            
