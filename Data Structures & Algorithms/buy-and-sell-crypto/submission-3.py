class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        buy= float('inf')
        for i in prices:
            buy = min(buy,i)
            profit = max(profit,  i - buy)
        
        return(profit)


        """
        input : List
        output: int
        goal : return maximum profit. If no profit found return 0

        Constraints
        - can array have negatives
        - can array be of length 1
        - what happens when no profit is made

        Tradeoffs
        use Two pointers
        - You are able use one pointer to capture the smallest amount to buy and another pointer to capture the largest day to sell. You can change pointers when there is a greater maximum

        approach:
        set profit to 0 
        set buy to
        loop through prices and set the smallest element to buy
        Then substract buy from prices[i] and set to profit
        Update profit if a larger amount is seen
        return profit
        """