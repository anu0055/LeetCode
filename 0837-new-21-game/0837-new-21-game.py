class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        P = [0.0]*(n+1)
        P[0] = 1

        curr_sum = 0 if k == 0  else 1
        for i in range(1, n+1):
            P[i] = curr_sum/maxPts
            if i < k:
                curr_sum += P[i]
            if i - maxPts >= 0 and i-maxPts < k:
                curr_sum -= P[i-maxPts]

        return sum(P[k:])