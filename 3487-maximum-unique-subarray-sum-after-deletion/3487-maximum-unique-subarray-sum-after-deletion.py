class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positive_num_set = set([num for num in nums if num > 0])
        return max(nums) if len(positive_num_set) == 0 else sum(positive_num_set)