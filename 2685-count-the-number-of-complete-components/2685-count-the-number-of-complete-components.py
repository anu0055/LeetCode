class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        groups = defaultdict(int)
        for vertex in range(n):
            adjList[vertex] = [vertex]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        for vertex in range(n):
            nei = tuple(sorted(adjList[vertex]))
            groups[nei] += 1

        return sum(1 for nei, freq in groups.items() if len(nei) == freq)
            
                