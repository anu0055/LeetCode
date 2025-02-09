class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        good_pairs = 0                  # good_pair:- i - nums[i] == j - nums[j]
        n = len(nums)
        for i, num in enumerate(nums):
            key = num - i                    # Calculating the pos - nums[pos] difference   
            good_pairs += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1    # Updating the map with same difference.

        return (n * (n - 1)) // 2 - good_pairs   # nC2 = n(n-1)/2 is for calculating total pairs
