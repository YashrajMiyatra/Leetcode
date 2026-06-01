class Solution:
    """
    Greedy Array Sorting approach for Minimum Cost of Buying Candies With Discount.
    
    Architecture:
    - **Concept**: To minimize the total cost, we must maximize the amount of "free" value we extract.
      Since the free candy must be cheaper than or equal to the minimum of the two paid candies, 
      the absolute best strategy is to group the most expensive candies together.
    - **Execution**: 
      1. Sort the `cost` array in descending order.
      2. Iterate through the array and pay for the 1st and 2nd candies, but take the 3rd one for free.
      3. This translates mathematically to ignoring every 3rd element (indices 2, 5, 8...).
    - Time Complexity: O(N log N) for sorting.
    - Space Complexity: O(1) auxiliary space.
    """
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        for i in range(len(cost)):
            # Ignore every 3rd candy (index 2, 5, 8...)
            if (i + 1) % 3 != 0:
                total += cost[i]
        return total
