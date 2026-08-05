class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        runningSum = nums[0]
        for num in nums[1:]:
            if runningSum > 0:
                runningSum += num
            else:
                runningSum = num
            
            ans = max(ans, runningSum)

        return ans