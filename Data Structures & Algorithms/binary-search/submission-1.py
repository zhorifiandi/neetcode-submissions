class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right and right < len(nums):
            mid_idx = (left + right) // 2
            mid = nums[mid_idx]
            if target == mid:
                return mid_idx
            elif target > mid:
                left = mid_idx + 1
            else:
                right = mid_idx - 1
        
        return -1