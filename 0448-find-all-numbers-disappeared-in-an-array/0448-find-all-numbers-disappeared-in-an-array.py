class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]* (n+1)
        ans = []
        for i in range(n):
            res[nums[i]] = 1
        for j in range(1, n+1):
            if res[j] == 0:
                ans.append(j)
        return ans
