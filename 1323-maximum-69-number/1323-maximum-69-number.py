class Solution:
    def maximum69Number (self, num: int) -> int:
        n = len(str(num))
        max_num = int("9"*n)
        diff = max_num - num
        pos_to_replace_from_back = len(str(diff))
        new_num = "9"*(n - pos_to_replace_from_back + 1) + str(num)[n - pos_to_replace_from_back + 1:]
        return int(new_num)
