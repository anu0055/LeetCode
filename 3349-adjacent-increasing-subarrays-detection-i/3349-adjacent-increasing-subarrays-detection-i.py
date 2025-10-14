class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            if len(nums) >= 2:
                return True
            else:
                return False
        i = 0
        while (i + k) < len(nums):
            curr = 1
            if nums[i] >= nums[i+1]:
                i += 1
                continue
            while i + 1 < len(nums) and nums[i] < nums[i+1]:
                curr += 1
                i += 1
            if k <= curr:
                if curr >= 2*k:
                    return True
                curr = 1
                i += 1
                while i + 1 < len(nums) and nums[i] < nums[i+1]:
                    curr += 1
                    i += 1
                if curr >= k:
                    return True
        return False 