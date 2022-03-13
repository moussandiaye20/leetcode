class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current=max(prices)
        maxP=0
        
        for i in  prices:
            if i<current:
                current=i
            else:
                maxP=max(maxP,i-current)
        return maxP
