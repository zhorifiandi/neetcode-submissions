
"""
minCost(0) = 0
minCost(1) = 0
minCost(2) = min(minCost(0) + cost(0), minCost(1) + cost(1))
minCost(3) = min(minCost(1) + cost(1), minCost(2) + cost(2))

"""

from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def minCost(target):
            if target <= 1:
                return 0
            
            return min(
                minCost(target-2) + cost[target-2],
                minCost(target-1) + cost[target-1],
            )
        
        return minCost(len(cost))