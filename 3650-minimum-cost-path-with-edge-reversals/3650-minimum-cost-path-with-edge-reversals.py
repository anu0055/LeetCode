import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        rev_graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            rev_graph[v].append((u, w))  # incoming edges

        INF = float('inf')
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = 0  # start at node 0, switch unused

        heap = [(0, 0, 0)]  # (cost, node, switch_used)

        while heap:
            cost, node, used = heapq.heappop(heap)

            if cost > dist[node][used]:
                continue

            # Normal edges
            for nxt, w in graph[node]:
                new_cost = cost + w
                if new_cost < dist[nxt][0]:
                    dist[nxt][0] = new_cost
                    heapq.heappush(heap, (new_cost, nxt, 0))

            # Reversed edges (only if switch unused)
            if used == 0:
                for nxt, w in rev_graph[node]:
                    new_cost = cost + 2 * w
                    if new_cost < dist[nxt][0]:
                        dist[nxt][0] = new_cost
                        heapq.heappush(heap, (new_cost, nxt, 0))

        ans = min(dist[n - 1])
        return ans if ans != INF else -1
