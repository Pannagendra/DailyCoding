"""
In a candy store, there are different types of candies available and prices[i] represent the price of  ith types of candies. You are now provided with an attractive offer.
For every candy you buy from the store, you can get up to k other different candies for free. Find the minimum and maximum amount of money needed to buy all the candies.
Note: In both cases, you must take the maximum number of free candies possible during each purchase.
"""

class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()
        
        # Minimum cost calculation
        min_cost = 0
        i, j = 0, len(prices) - 1
        while i <= j:
            min_cost += prices[i]
            i += 1      # bought candy
            j -= k      # take k most expensive for free
        
        # Maximum cost calculation
        prices.sort(reverse=True)
        max_cost = 0
        i, j = 0, len(prices) - 1
        while i <= j:
            max_cost += prices[i]
            i += 1      # bought candy
            j -= k      # take k cheapest for free
        
        return [min_cost, max_cost]
