class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = {i:[] for i in range(n)}
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        print(adj)
        visit = set()


        def dfs(node,parent):
            if node in visit:
                return False
            visit.add(node)
            

            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour,node):
                    return False
          
            return True
        

        return dfs(0,-1) and len(visit) == n
        