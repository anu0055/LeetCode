class Solution:
    def countGoodNumbers(self, n: int):
        mod = 10**9+7
        total_even_positions = (n + 1) // 2
        total_odd_positions = n // 2

        tot_comb = (pow(5, total_even_positions, mod) * pow(4, total_odd_positions, mod)) % mod
        return tot_comb