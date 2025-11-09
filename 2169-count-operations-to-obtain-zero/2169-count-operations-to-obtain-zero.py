class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        op = 0
        if num1 == 0 or num2 == 0:
            return 0
        while num1 > 0 or num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            op += 1
            if num1 == 0 or num2 == 0:
                break
        return op