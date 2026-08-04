class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj ={i: [] for i in range(numCourses)}
        for src,dst in prerequisites:
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
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
        
        