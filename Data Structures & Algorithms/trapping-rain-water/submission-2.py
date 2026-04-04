class Solution:
    def trap(self, height: List[int]) -> int:
        # highest wall, from current index to the left
        prefixMax = [0]
        # highest wall, from current index to the right
        suffixMax = [0]
        n = len(height)
        for i in range(n):
            prefixMax.append(max(prefixMax[-1], height[i]))
            suffixMax.insert(0, max(suffixMax[0], height[n-i-1]))
        
        # print(prefixMax)
        # print(suffixMax)

        water = 0
        # ans = []
        for i in range(n):
            water += max(0, min(prefixMax[i], suffixMax[i]) - height[i])
        #     ans.append(water)
        
        # print(ans)

        # 
        #               x
        #       x       x x   x
        # . x . x x . x x x x x x 

        return water