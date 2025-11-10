class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == 0:
                i += 1
                continue
            j = i
            while j < n and nums[j] != 0:
                j += 1
            block_min = min(nums[i:j])
            for k in range(i, j):
                if nums[k] == block_min:
                    nums[k] = 0
            ops += 1
            continue  # re-check same block
        return ops