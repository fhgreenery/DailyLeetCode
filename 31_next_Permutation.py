class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # lexicographical larger rearrangement
        found = False
        for i in range(len(nums)-1, 0, -1): # from n-1 to 0
            if nums[i] > nums[i-1]:
                nums[i:] = nums[i:][::-1] 
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break

                found = True
                break
        if not found: nums.reverse()
        return nums

if __name__ == "__main__":
    nums = [1, 2, 3]
    s = Solution()
    res = []
    res = s.nextPermutation(nums)
    print(res)
