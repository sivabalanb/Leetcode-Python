#121. Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = max(prices), 0
        
        for val in prices:
            if val < min_price:
                min_price = val
            max_profit = max(max_profit, val - min_price)
            # elif val - min_price > max_profit:
            #     max_profit = val - min_price
            #print(f"val {val} min_price {min_price} max_profit {max_profit}")
                
        return max_profit