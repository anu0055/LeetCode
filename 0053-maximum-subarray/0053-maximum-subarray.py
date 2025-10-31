class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            curr += num
            if curr < 0:
                curr = 0
            res = max(res, curr)
        return res
