class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 1000000007
        powers = []
        binary_rep = bin(n)[2:]
        i = 0
        for b in list(binary_rep)[::-1]:
            if int(b) != 0:
                powers.append(int(b)*(2**i)) 
                i += 1
            else:
                i += 1
        ans = []
        for start, end in queries:
            prod = 1
            for i in range(start, end+1):
                prod *= powers[i]
            ans.append(prod%mod)
        return ans

        