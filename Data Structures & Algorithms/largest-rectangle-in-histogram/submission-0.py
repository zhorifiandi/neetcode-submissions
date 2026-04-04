class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        stack = []

        maxArea = 0

        for i in range(n):
            h = heights[i]
            start = i
            while stack and h < stack[-1][1]:
                left_idx, left_h = stack.pop()
                maxArea = max(maxArea, left_h * (i-left_idx))
                start = left_idx
            
            stack.append((start, h))
        
        return maxArea
