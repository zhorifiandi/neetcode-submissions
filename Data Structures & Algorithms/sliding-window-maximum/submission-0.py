from heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        index = dict()
        h = []
        n = len(nums)

        ans = []

        left = right = 0
        for i in range(n):
            heappush(h, -nums[i])
            index[nums[i]] = i
            if right - left + 1 < k:
                right += 1
            else:
                maxVal = -h[0]
                while not left <= index[maxVal] <= right:
                    heappop(h)
                    maxVal = -h[0]
                
                ans.append(maxVal)
                
                left += 1
                right += 1
            
        
        return ans