class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stk = ['1']
        n = 1
        res = ''
        for char in pattern:
            if char == 'I':
                while stk:
                    res += stk.pop()
            
            n += 1
            stk.append(str(n))

        return res + ''.join(stk[::-1])
        

