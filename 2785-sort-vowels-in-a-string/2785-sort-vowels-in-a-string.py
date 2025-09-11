class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        res = [0]*n
        vw = []
        for i, ch in enumerate(list(s)):
            if ch not in "aeiouAEIOU":
                res[i] = ch
            else:
                vw.append(ch)
        vw.sort(key=lambda x: ord(x))
        for i in range(len(res)):
            if res[i] == 0:
                res[i] = vw.pop(0)
        return "".join(res)

