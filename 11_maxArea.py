class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # height = [1,8,6,2,5,4,8,3,7]
        maxArea = 0
        n = len(height)
        i, j = 0, n-1
        while j > i:
            area = min(height[i], height[j])* (j - i)
            maxArea = max(area, maxArea)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    print(s.maxArea(height))
