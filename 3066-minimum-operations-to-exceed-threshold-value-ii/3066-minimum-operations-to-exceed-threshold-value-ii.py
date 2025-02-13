class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        min_operations = 0
        
        while nums[0] < k and len(nums) >=2:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            heapq.heappush(nums, min(x, y)*2 + max(x, y))
            min_operations += 1
        return min_operations
