"""
maxCash(0) = nums[0]
maxCash(1) = max(nums[0], nums[1])
maxCash(2) = max(maxCash(0) + nums[2], maxCash(1))
"""
from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def maxCash(index):
            if index == 0:
                return nums[0]
            elif index == 1:
                return max(nums[0], nums[1])
            else:
                return max(
                    maxCash(index-2) + nums[index],
                    maxCash(index-1)
                )

        
        return maxCash(len(nums) - 1)