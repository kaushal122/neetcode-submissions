class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        sell=prices[0]
        profit=0
        for pr in prices:
            if pr<=buy:
                #profit=max(profit,sell-buy)
                buy=pr
            elif pr-buy>profit:
                profit=pr-buy
                sell=pr
        
        return profit
