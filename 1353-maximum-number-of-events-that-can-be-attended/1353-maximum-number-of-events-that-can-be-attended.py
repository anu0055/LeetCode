class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key = lambda x : x[0])
        max_day = max(event[1] for event in events)
        pq = []
        ans, j = 0, 0
        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heappop(pq)
            if pq:
                heappop(pq)
                ans += 1
        return ans
