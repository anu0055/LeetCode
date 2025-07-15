class Solution:
    def isValid(self, word: str) -> bool:
        vow = 0
        cons = 0
        if len(word) < 3:
            return False
        for ch in word:
            if ch in "@#$":
                return False
            if ch not in "aeiouAEIOU" and ch not in "@#$" and ch not in "0987654321":
                cons += 1
            elif ch in "aeiouAEIOU" and ch not in "@#$" and ch not in "0987654321":
                vow += 1
                
        if cons >= 1 and vow >= 1:
            return True
        return False