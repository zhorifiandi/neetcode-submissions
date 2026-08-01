class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # getCombs([],[2,5,6,9])
        # -> 2: getCombs([2],[2,5,6,9])
        #      -> 2: getCombs([2,2],[2,5,6,9])
        #           -> 2: getCombs([2,2,2],[2,5,6,9])
        #               -> 2: getCombs([2,2,2,2],[2,5,6,9]) 
        #                   => stop (no possible ans)
        #           -> 5 == 9 => return [2,2,5]
        #           -> 6 x
        #           -> 9 x
        #      -> 5: getCombs([2,5],[5,6,9])
        #           -> stop ( no possible ans)

        nums.sort()
        def getCombs(base, nums):
            answers = []
            curSum = sum(base)
            for i in range(len(nums)):
                if curSum + nums[i] == target:
                    answers.append(base + [nums[i]])
                    break
                
                if curSum + nums[i] < target:
                    answers.extend(getCombs(base + [nums[i]], nums[i:]))
            
            return answers

        return getCombs([], nums)
