class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        total_odd_positions = n // 2
        total_even_positions = (n+1) // 2

        total_comb = (pow(4,total_odd_positions) * pow(5, total_even_positions)) % mod
        return total_comb