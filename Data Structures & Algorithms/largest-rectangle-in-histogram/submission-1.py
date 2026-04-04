class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # [1,3,4,5,2]
        # i=0 [(0,1)] 
        # i=1 [(0,1),(1,3)] 
        # i=2 [(0,1),(1,3),(2,4)] 
        # i=3 [(0,1),(1,3),(2,4), (3,5)] 
        # i=4 [(0,1), (1,2)] ans = 8 = max(0, (4-3)*5, (4-2)*4, (4-1)*3)
        # i=n=5 , ans = 8 = max(8, (5-0)*1, (5-1) * 2)

        heights.append(0)
        ans = 0
        stack = []
        n = len(heights)
        for i in range(n):
            h = heights[i]
            left_most_idx = i
            while stack and h < stack[-1][1]:
                j, left_h = stack.pop()
                ans = max(ans, (i-j) * left_h)
                left_most_idx = j
            
            stack.append((left_most_idx, h))

        heights.pop()
        return ans