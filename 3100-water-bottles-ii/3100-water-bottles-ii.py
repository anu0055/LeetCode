class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty = 0
        
        while numBottles > 0:
            # Drink all current full bottles
            ans += numBottles
            empty += numBottles
            numBottles = 0

            # Exchange empties if possible
            if empty >= numExchange:
                empty -= numExchange
                numBottles += 1
                numExchange += 1
            else:
                break
                
        return ans
