class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        curr_str = ""
        sequence = []
        def backtrack(n, curr, sequence):
            if len(curr) == n:
                sequence.append(curr)
                return 
            for curr_char in ['a', 'b', 'c']:
                if len(curr) > 0 and curr[-1] == curr_char:
                    continue
                backtrack(n, curr + curr_char, sequence)

        backtrack(n, curr_str, sequence)
        if len(sequence) < k:
            return ""
        sequence.sort()
        return sequence[k-1]