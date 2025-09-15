class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        set_ = set(list(brokenLetters))
        text_ = text.split(" ")
        count = len(text_)
        for word in text_:
            for c in word:
                if c in set_:
                    count -= 1
                    break

        return count