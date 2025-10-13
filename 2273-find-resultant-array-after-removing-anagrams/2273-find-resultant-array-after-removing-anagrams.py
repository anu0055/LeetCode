from collections import Counter, defaultdict
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        idx_count = []
        new_words = []
        for idx, word in enumerate(words):
            new_words.append("".join(sorted(word)))
        for idx,word in enumerate(new_words):
            if not res or word != res[-1]:
                res.append(word)
                idx_count.append(idx)
        return [words[i] for i in idx_count]

                
        
           