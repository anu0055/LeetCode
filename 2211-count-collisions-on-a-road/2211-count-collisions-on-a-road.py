class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0

        for d in directions:
            if d == 'R':
                stack.append('R')

            elif d == 'S':
                while stack and stack[-1] == 'R':
                    collisions += 1
                    stack.pop()
                stack.append('S')

            else:  # 'L'
                if not stack:
                    stack.append('L')
                else:
                    if stack[-1] == 'S':
                        collisions += 1
                        stack.append('S')

                    elif stack[-1] == 'R':
                        # First collision R <-> L gives +2
                        collisions += 2
                        stack.pop()

                        # pop additional Rs behind → each gives +1
                        while stack and stack[-1] == 'R':
                            collisions += 1
                            stack.pop()

                        # 🚨 FIX: After handling all R's, ONLY THEN add 'S'
                        stack.append('S')

                    else:  # stack[-1] == 'L'
                        stack.append('L')

        return collisions
