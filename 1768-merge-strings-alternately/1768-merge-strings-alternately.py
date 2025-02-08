class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        n1 = len(word1)
        n2 = len(word2)

        n = min(n1, n2)
        for i in range(n):
            res += word1[i]
            res += word2[i]
        if len(word1) > n:
            res += word1[n:]
        if len(word2) > n:
            res += word2[n:]
        return res        