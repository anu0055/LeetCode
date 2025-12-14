class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        total_seats = len(seats)
        
        # Must have even number of seats and at least one section
        if total_seats == 0 or total_seats % 2 != 0:
            return 0
        
        ways = 1
        
        # Iterate over pairs of seat-pairs
        for i in range(2, total_seats, 2):
            left = seats[i - 1]
            right = seats[i]
            
            # Plants between two consecutive seat-pairs
            plants_between = right - left - 1
            ways = (ways * (plants_between + 1)) % MOD
        
        return ways

        