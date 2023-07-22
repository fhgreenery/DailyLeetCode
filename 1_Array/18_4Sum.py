class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # twoSum: dict
        # threeSum: two pointers

        results = []
        nums.sort()
        for i in range(len(nums)-3):
            if i == 0 or nums[i] != nums[i-1]: # ¬p: if i > 0 and nums[i] == nums[i-1] 
                threeResult = self.threeSum(nums[i+1:], target-nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()

        for i in range(len(nums)-2):
            lo, hi = i + 1, len(nums) - 1

            if i == 0 or nums[i] != nums[i-1]:
                while lo < hi:
                    sum3 = nums[i] + nums[lo] + nums[hi]
                    if sum3 == target:
                        res.append([nums[i], nums[lo], nums[hi]]) #()
                        while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                        lo += 1; hi -=1
                    elif sum3 < target:
                        lo += 1
                    else:
                        hi -= 1
        return res

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    s = Solution()
    print(s.fourSum(nums,target))


