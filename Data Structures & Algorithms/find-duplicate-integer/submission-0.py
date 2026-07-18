class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [5,3,2,4,4]
        # [4,3,2,4,5]
        # [4,3,2,4,5] => collision return 4


        # [5,3,2,1,1] i = 0 -> swap
        # [1,3,2,1,5] i = 0
        # [1,2,3,1,5] i = 1 -> swap
        # [1,2,3,1,5] i = 2 
        # [1,2,3,1,5] i = 3 -> collision, return 1


        curIdx = 0
        while curIdx < len(nums):
            # print(curIdx, nums)
            curNum = nums[curIdx]
            if curNum - 1 == curIdx:
                curIdx += 1
                continue

            if nums[curNum - 1] == curNum:
                return curNum
            
            

            # swap
            toSwap = nums[curNum - 1]
            nums[curNum - 1] = curNum
            nums[curIdx] = toSwap
        

        return 0