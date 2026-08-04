"""
n = len(nums)
maxCash = max (getMaxCash(true, n), getMaxCash(false, n) )

"""

from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        @cache
        def getMaxCash(start, target):
            if target < start:
                return 0
            
            if start == target:
                return nums[target]
            
            return max(
                getMaxCash(start, target - 2) + nums[target],
                getMaxCash(start, target - 1)
            )


        return max(
            getMaxCash(1, n-3) + nums[n-1],
            getMaxCash(0, n-2),
        )