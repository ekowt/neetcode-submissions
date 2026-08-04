class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set ()
        while n  not in visit:
            visit.add(n)
            n = self.arr(str(n))
            if n ==1:
                return True
        return False



    def arr(self,n):
        total = 0
        for i in n:
            total += int(i)**2
        return total


