class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) <= 1:
            return True
        elif bits[-2] == 0:
            return True
        return False