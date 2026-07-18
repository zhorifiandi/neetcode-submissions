class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            targetIdx = abs(nums[i]) - 1
            if nums[targetIdx] < 0:
                return targetIdx + 1
            
            nums[targetIdx] *= -1
        
        return 0