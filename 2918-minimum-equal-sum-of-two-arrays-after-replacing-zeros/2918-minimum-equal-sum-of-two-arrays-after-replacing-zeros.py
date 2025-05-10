class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero_count_1 = nums1.count(0)
        zero_count_2 = nums2.count(0)
        sum_1 = sum(nums1) + zero_count_1
        sum_2 = sum(nums2) + zero_count_2

        if(zero_count_1 == 0 and sum_2 > sum_1) or (zero_count_2 == 0 and sum_1 > sum_2):
            return -1

        return max(sum_1, sum_2)
