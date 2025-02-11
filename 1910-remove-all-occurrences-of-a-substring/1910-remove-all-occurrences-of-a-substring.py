class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part) # 3
        for i in range(len(s)):
            if len(stack) >= n and stack[-len(part):] == list(part):
                for _ in range(n):
                    stack.pop()
            stack.append(s[i])
        if len(stack) >= n and stack[-len(part):] == list(part):
                for _ in range(n):
                    stack.pop()

        return ''.join(stack)