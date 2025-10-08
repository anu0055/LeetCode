class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        potions.sort()
        pairs = [0]*n
        
        def bs(idx, potions):
            l = 0
            r = m-1
            if spells[idx] * potions[-1] < success:
                pairs[idx] = 0
            else:
                while (l < r):
                    mid = (l + r)//2
                    if potions[mid]*spells[idx] < success:
                        l = mid + 1
                    elif potions[mid]*spells[idx] >= success:
                        r = mid
                pairs[idx] = m - r

        for i in range(n):
            bs(i, potions)
        
        return pairs 
