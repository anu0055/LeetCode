from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:   # skip duplicate i
                continue
            target = -nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    # skip duplicate nums[j]
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    # skip duplicate nums[k]
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
        return res
