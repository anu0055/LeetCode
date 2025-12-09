class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9+7
        count = defaultdict(list)
        res = 0
        for i, n in enumerate(nums):
            count[n].append(i)
        for j in range(len(nums)):
            low_idx = 0
            high_idx = 0
            if nums[j]*2 in count:
                for idx in count[nums[j]*2]:
                    if idx < j:
                        low_idx += 1
                    if idx > j:
                        high_idx += 1
            res += (low_idx * high_idx)%mod
        return res%mod
