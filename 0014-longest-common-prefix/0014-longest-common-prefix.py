class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = strs[0]
        res = ""
        for i in range(1, len(strs)):
            if len(strs[i]) < len(smallest):
                smallest = strs[i]
        
        for i in range(len(smallest)):
            count = 0
            ch = smallest[i]
            for str_ in strs:
                if str_[i] != ch and count == 0:
                    break
                elif str_[i] != ch and count :
                    return smallest[:i]
                else:
                    count += 1
            if count != len(strs):
                break
            else:
                res += ch
        return res