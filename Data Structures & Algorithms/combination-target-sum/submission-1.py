class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        def getNextCombinations(base, start):
            solutions = []
            curSum = sum(base)
            for i in range(start, len(nums)):
                if curSum + nums[i] == target:
                    solutions.append(base + [nums[i]])
                    break
                
                if curSum + nums[i] < target:
                    solutions.extend(
                        getNextCombinations(base + [nums[i]], i)
                    )
            
            return solutions

        return getNextCombinations([], 0)