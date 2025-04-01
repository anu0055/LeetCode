class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        
        for idx in range(n - 1, -1, -1):
            points, power = questions[idx]
            nextIdx = idx + power + 1  
            dp[idx] = max(points + (dp[nextIdx] if nextIdx < n else 0), dp[idx + 1])

        return dp[0]