class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Counter for keeping track of elements other than val
        count = 0
        # Loop through all the elements of the array
        for i in range(len(nums)):
            # If the element is not val
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
'''
        while val in nums :
	        nums.remove(val)
        return len(nums)
'''

if __name__ == "__main__":
	nums = [3,2,2,3]
	val = 3
	print(Solution().removeElement(nums,val))
