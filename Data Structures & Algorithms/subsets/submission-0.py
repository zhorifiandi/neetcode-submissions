class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def expand(baseItems, nums):
            # print("expand", baseItems, nums)
            globalExpansion = []
            for i in range(len(nums)):
                expansion = []
                for base in baseItems:
                    expansion.append(base + [nums[i]])
                
                globalExpansion += expand(expansion, nums[i+1:])
            ans = baseItems + globalExpansion
            return ans
        
        return expand([[]], nums)