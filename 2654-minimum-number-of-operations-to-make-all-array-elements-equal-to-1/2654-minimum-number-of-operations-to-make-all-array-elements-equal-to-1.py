class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 in nums:
            count = nums.count(1)
            return n - count
        min_L = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_L = min(min_L, j - i + 1)
                    break
        if min_L == float('inf'):
            return -1
        return n + min_L - 2