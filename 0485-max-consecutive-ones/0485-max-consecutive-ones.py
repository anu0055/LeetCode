class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ = float(-inf)
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
            max_ = max(max_, count)
        return max_
