class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        res = []

        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                sum3 = nums[i] + nums[lo] + nums[hi]
                if sum3 == 0:
                    res.append((nums[i], nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
                    while nums[lo] == nums[lo - 1] and lo < hi:
                        lo += 1
                    while nums[hi] == nums[hi + 1] and lo < hi:
                        hi -= 1
                elif sum3 < 0:
                    lo += 1
                else:
                    hi -= 1

        return res

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    s = Solution()
    res_list = []    

    res_list.append(s.threeSum(nums))
    print(res_list)
	
