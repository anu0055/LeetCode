class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        max_ = max([freq[val] for val in freq])
        for _, count in freq.items():
            if count == max_:
                res += count
        return res 