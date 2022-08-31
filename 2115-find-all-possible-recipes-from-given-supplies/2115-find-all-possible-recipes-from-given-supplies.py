class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        indegree = {}
        queue = deque(supplies)
        ans = []
        recip = set(recipes)
        for i, recipe in enumerate(recipes):
            graph[recipe] = set(ingredients[i])
            indegree[recipe] = len(ingredients[i])
            
        while queue:
            curr = queue.popleft()
            if curr in recip:
                ans.append(curr)
            for key in graph:
                if curr in graph[key]:
                    indegree[key] -= 1
                    if indegree[key] == 0:
                        queue.append(key)
        return ans
                
        
        