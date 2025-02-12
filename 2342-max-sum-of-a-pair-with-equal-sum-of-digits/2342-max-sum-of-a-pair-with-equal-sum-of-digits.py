class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(num: int):
            nums = list(str(num))
            return sum(int(i) for i in nums)

        Hashmap = defaultdict(list)
        for num in nums:
            digit_sum = digitSum(num)
            Hashmap[digit_sum].append(num)
        if len(Hashmap) == len(nums):
            return -1
        max_sum = 0
        for digit in Hashmap.values():
            heap = [-i for i in digit]
            if len(heap) >= 2: 
                heapq.heapify(heap)
                first = -heapq.heappop(heap)
                sec = -heapq.heappop(heap)
                max_sum = max(max_sum, first+sec)
        return max_sum
             
