class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""
        expected_length = 2**(len(nums[0]))
        num_occ = [0]*(expected_length)
        for bin_num in nums:
            bin_to_int = int(bin_num, 2)
            num_occ[bin_to_int] = 1
        if expected_length == 4 and num_occ[0] == 0:
            return "00"
        for i in range(expected_length):
            if num_occ[i] == 0:
                res = bin(i)
                if len(res) != len(nums[0]):
                    res += "0"*(len(nums[0])-len(res))
        return res[2:]

