class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if len(candies) < k:
            return 0
        min_candies = min(candies)
        count = 0
        for i in range(len(candies)):
            if candies[i] >= min_candies:
                count += 1
        return min_candies