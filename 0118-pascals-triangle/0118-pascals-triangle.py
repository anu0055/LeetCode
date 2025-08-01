class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1], [1,1]]
        for i in range(1, numRows-1):
            cur_lst = [1] + [0]*(i) + [1]
            for j in range(1, len(cur_lst)-1):
                cur_lst[j] = res[-1][j-1] + res[-1][j]
            res.append(cur_lst)
        return res
