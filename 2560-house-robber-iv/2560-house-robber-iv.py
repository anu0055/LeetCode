class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        def isPossible(nums, mid, k):
            houses = 0
            i = 0
            while i < (len(nums)):
                if nums[i] <= mid:
                    houses += 1
                    i += 1
                i += 1
            return houses >= k
        
        l = min(nums)
        r = max(nums)

        res = r
        while l <= r:
            mid = (l + r)//2

            if isPossible(nums, mid, k):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res