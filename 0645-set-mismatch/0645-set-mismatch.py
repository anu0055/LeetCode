class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        original = (n * (n+1))//2
        current = sum(set(nums))
        current_total = sum(nums)
        left_out = original - current
        duplicate = left_out - (original - current_total)
        return [duplicate, left_out]