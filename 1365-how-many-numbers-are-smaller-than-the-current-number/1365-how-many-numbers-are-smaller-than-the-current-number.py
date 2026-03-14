class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            ans = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    ans += 1
            res.append(ans)
        return res
