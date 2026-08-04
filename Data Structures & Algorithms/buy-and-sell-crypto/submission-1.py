class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        profit = 0
        mini = sys.maxsize

        for i in prices:
            if i<mini: 
                mini = i
            if i-mini > profit:
                profit = i-mini
        return(profit)