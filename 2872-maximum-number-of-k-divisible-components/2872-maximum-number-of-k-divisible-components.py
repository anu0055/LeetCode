class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adjList = [[] for _ in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adjList[u].append(v)
            adjList[v].append(u)

        componentCount = [0]
        def dfs(curr_node, parentNode, adjList, node_value, k, componentCount):
            sum1 = 0
            for NeiNode in adjList[curr_node]:
                if NeiNode != parentNode:
                    sum1 += dfs(NeiNode, curr_node, adjList, node_value, k, componentCount)
            sum1 += node_value[curr_node]
            if sum1 % k == 0:
                componentCount[0] += 1
            return sum1
        dfs(0, -1, adjList, values, k, componentCount)
        return componentCount[0]

        
