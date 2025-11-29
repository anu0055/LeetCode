class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for num in nums:
            ans += num%k
        return ans%k