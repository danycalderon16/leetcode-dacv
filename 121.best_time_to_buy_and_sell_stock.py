from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day_to_buy = [1, prices[0]]
        for i, price in enumerate(prices, start=1):
            if price < day_to_buy[1]: #position 1
                day_to_buy[0] = i
                day_to_buy[1] = price

        day_to_sell = [day_to_buy[0], day_to_buy[1]]
        for i, price in enumerate(prices[day_to_buy[0]:], start=day_to_buy[0]):
            if price > day_to_sell[1]:
                day_to_sell[0] = i
                day_to_sell[1] = price
                
        return day_to_sell[1] - day_to_buy[1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))