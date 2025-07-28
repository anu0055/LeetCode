class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        def subset_or(subset):
            or_value = 0
            for num in subset:
                or_value |= num
            return or_value
        n = len(nums)
        count = 0
        for i in range(1, 1 << n):
            current_or = 0
            for j in range(n):
                if i & (1 << j):
                    current_or |= nums[j]
            if current_or == max_or:
                count += 1
        return count