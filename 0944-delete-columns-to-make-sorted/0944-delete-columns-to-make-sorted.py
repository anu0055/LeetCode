class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        delete_count = 0
        
        # Check each column
        for j in range(cols):
            for i in range(1, rows):
                # If current character is less than previous in same column
                if strs[i][j] < strs[i-1][j]:
                    delete_count += 1
                    break  # No need to check further rows for this column
        
        return delete_count