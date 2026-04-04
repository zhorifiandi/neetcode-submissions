class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        loc = {}
        for i in range(len(nums)):
            if target - nums[i] in loc:
                return [loc[target - nums[i]], i]

            loc[nums[i]] = i

        return []