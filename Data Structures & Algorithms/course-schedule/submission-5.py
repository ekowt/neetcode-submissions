class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj ={i: [] for i in range(numCourses)}
        for src,dst in prerequisites:
            adj[src].append(dst)

        visit= set()
       
        
        def dfs(node):
            if node in visit:
                return False
            if adj[node] == []:
                return True
                    
            visit.add(node)
            for neighbour in adj[node]:
                if not dfs(neighbour):
                    return False
            visit.remove(node)
            adj[node] = []
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
        
        