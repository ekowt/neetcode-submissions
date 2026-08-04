class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set ()
        while n  not in visit:
            visit.add(n)
            n = self.arr((n))
            if n ==1:
                return True
        return False



    def arr(self,n):
        total = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            total += digit
            n = n // 10
        return total


