class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Runtime: Beats 79.87%of users with Python; Memory: Beats 21.58%of users with Python
        """
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi)//2 # mid. = lo + (hi - lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2
    s = Solution()
    print("the result is", s.searchInsert(nums, target))