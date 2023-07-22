class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # closest: 
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                sum3 = nums[i] + nums[lo] + nums[hi]
                if sum3 == target:
                    return target
                if abs(sum3 - target) < abs(res - target):
                    res = sum3
                if sum3 < target:
                    lo += 1
                else:
                    hi -= 1

        return res

if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 1
    s = Solution()
    print(s.threeSumClosest(nums, target))
