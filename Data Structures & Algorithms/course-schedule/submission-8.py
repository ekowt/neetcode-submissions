class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = {i: [] for i in range(numCourses)}

        for src,dst in prerequisites:
            adj_list[src].append(dst)
        
        visit = set()
        
        def dfs(node):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj_list[node]:
                if  not dfs(nei):
                    return False
            visit.remove(node)
            return True
            

        
        for node in adj_list:
            if not dfs(node):
                return False
        return True