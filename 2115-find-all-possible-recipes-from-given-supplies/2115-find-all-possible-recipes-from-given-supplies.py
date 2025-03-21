from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        supplySet = set(supplies)

        for idx in range(len(recipes)):
            recipe = recipes[idx]
            reqIng = ingredients[idx]
            cnt = 0
            for ing in reqIng:
                if ing not in supplySet:
                    graph[ing].append(recipe)
                    cnt += 1
            inDegree[recipe] = cnt

        queue = deque()
        res = []
        for recipe in recipes:
            if inDegree[recipe] == 0:
                queue.append(recipe)

        queue.extend(supplies)

        while queue:
            item = queue.popleft()
            if item in recipes:
                res.append(item)
            for nei in graph[item]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
        return res