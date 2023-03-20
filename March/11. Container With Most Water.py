class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, Max = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                Max = max(Max, height[i] * (j - i))
                i += 1
            else:
                Max = max(Max, height[j] * (j - i))
                j -= 1
        return Max
