class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = sys.maxsize
        profit = 0


        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
                print(mini)
            if prices[i] - mini > profit:
                profit = prices[i] - mini
        
        return(profit)
        
       


