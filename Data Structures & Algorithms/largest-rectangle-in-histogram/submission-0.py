class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, height in enumerate(heights):
            last_i = i
            while stack and stack[-1][1] > height:
                p = stack.pop()
                last_i = p[0]
                maxArea = max(maxArea, (i-p[0]) * p[1])
            stack.append((last_i, height))
        i = len(heights)
        while stack:
            p = stack.pop()
            maxArea = max(maxArea, (i-p[0]) * p[1])
        return maxArea
        