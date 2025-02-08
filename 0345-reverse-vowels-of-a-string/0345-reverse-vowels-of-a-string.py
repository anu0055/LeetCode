class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        vowel = "aeiouAEIOU"
        st = list(s)
        while i < j:
            if st[i] in vowel and st[j] in vowel:
                temp = st[i]
                st[i] = st[j]
                st[j] = temp
                i+=1
                j-=1
            if st[i] not in vowel:
                i+=1
            if st[j] not in vowel:
                j-=1
        
        return "".join(st)