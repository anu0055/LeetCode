class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_peri = 0
        for i in range(1, len(nums)-1):
            if nums[i] + nums[i-1] > nums[i+1]:
                max_peri = max(max_peri, nums[i-1]+nums[i]+nums[i+1])
        return max_peri