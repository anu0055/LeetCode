class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        right = defaultdict(int)
        left = defaultdict(int)
        res = 0

        # total frequency
        for n in nums:
            right[n] += 1

        for j in range(len(nums)):
            # current j is moving from right to left
            right[nums[j]] -= 1

            target = nums[j] * 2
            if target in left and target in right:
                res = (res+ left[target] * right[target]) % mod

            left[nums[j]] += 1

        return res
    # Brute force with 1114/1121 test passing
    #def specialTriplets(self, nums: List[int]) -> int:
        # mod = 10**9+7
        # count = defaultdict(list)
        # res = 0
        # for i, n in enumerate(nums):
        #     count[n].append(i)
        # for j in range(len(nums)):
        #     low_idx = 0
        #     high_idx = 0
        #     if nums[j]*2 in count:
        #         for idx in count[nums[j]*2]:
        #             if idx < j:
        #                 low_idx += 1
        #             if idx > j:
        #                 high_idx += 1
        #     res += (low_idx * high_idx)%mod
        # return res%mod
