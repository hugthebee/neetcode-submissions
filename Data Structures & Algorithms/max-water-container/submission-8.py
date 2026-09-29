class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        ans = 0

        while i < j:
            ans = max(ans, min(heights[i], heights[j]) * (j - i))

            if heights[i + 1] > heights[i] or heights[i] <= heights[j]:
                i+=1
            elif heights[j - 1] > heights[j] or heights[j] <= heights[i]:
                j-=1
            else: 
                i+=1
                j-=1

        return ans

