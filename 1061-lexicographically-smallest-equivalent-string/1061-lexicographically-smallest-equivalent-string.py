class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adjList = defaultdict(list)
        for u, v in zip(s1, s2):
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(ch, visited):
            visited.add(ch)
            min_char = ch
            for neighbour in adjList[ch]:
                if neighbour not in visited:
                    next_char = dfs(neighbour, visited)
                    min_char = min(min_char, next_char)
            return min_char
        
        res = []
        for ch in baseStr:
            visited = set()
            res.append(dfs(ch, visited))
        return "".join(res)
