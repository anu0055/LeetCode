class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums) % p
        if rem == 0:
            return 0
        n = len(nums)
        res = n
        subsum = {0: -1}
        t = 0
        for i in range(n):
            t = (t + nums[i]) % p
            subsum[t] = i
            pair = (t - rem) % p
            if pair in subsum:
                res = min(res, i - subsum[pair])
        return res if res < n else -1