class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        size = sys.maxsize
        profit = 0

        for num in prices:
            if num  < size:
                size = num
            if num - size  > profit:
                profit  = num - size
        return(profit)