class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        maxx = float('-inf')
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            maxx = max(maxx, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxx
            
            