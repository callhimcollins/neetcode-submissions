class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = float('-inf')
        l, r = 0, n-1

        while l < r:
            width = (r - l)
            height = min(heights[l], heights[r])
            maxArea = max(maxArea, (width * height))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea
