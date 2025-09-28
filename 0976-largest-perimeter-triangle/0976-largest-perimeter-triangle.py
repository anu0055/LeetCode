class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        max_peri = 0
        for i in range(len(nums)-2):
            a = nums[i]
            for j in range(i+1, len(nums)-1):
                b = nums[j]
                for k in range(j+1, len(nums)):
                    c = nums[k]

                    if (a+b > c) and (b+c > a) and (c+a > b):
                        max_peri = max(max_peri, a+b+c) 
        return max_peri