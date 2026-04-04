class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                ans.append((nums[left], nums[right]))

            if nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

        return ans
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            otherTwos = self.twoSum(nums[i+1:], -nums[i])
            for ot in otherTwos:
                ans.add((nums[i], ot[0], ot[1]))
        
        return list(ans)