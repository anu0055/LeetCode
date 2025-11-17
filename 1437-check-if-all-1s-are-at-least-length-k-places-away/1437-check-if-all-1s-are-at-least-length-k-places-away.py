class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                j = i + 1
                while j < len(nums) and nums[j] != 1:
                    j += 1
                if j - i - 1 >= k and j == len(nums)-1:
                    return True
                else:
                    i = j - 1
            i += 1
        return False
