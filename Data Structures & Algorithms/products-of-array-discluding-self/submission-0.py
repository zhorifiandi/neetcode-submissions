class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1]
        suffixProduct = [1]

        for i in range(len(nums)):
            prefixProduct.append(prefixProduct[-1] * nums[i])
            suffixProduct.insert(0, suffixProduct[0] * nums[len(nums)-1-i])
        

        ans = []
        for i in range(len(nums)):
            ans.append(
                prefixProduct[i] * suffixProduct[i+1]
            )

        return ans