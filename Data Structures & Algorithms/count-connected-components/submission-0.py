class Union:
    def __init__(self,n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    

    def find(self,n):
        if self.par[n] != n:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1==p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p2]  = p1
            self.rank[p2] += 1
        return True
        


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = Union(n)
        res = n
        for src, dst in edges:
            if adj.union(src,dst):
                res-=1
        return(res)




        