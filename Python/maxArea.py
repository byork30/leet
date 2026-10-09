class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0,0
        maxArea = 0
        while i < len(height):
            if height[i] == 0 or maxArea // height[i] >= len(height):
                i += 1
                continue
            j = i + 1
            while j < len(height):
                if min(height[i], height[j]) * (j-i) > maxArea:
                    maxArea = min(height[i], height[j]) * (j-i)
                j += 1
            i += 1
        return maxArea
