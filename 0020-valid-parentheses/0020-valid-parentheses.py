class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) <= 1:
            return False
        for ch in s:
            if stack and ch == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and  ch == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and ch == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0
