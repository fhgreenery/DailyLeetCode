
class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dicts = {}
        for i in range(len(nums)):
            if target - nums[i] in dicts:
                return [dicts[target - nums[i]],i]
            else:
                dicts[nums[i]]=i

if __name__ == "__main__":
    idx = []
    nums = [2,7,11,15]
    target = 9
    s = Solution()
    idx.append(s.twoSum(nums, target)) 
    print(idx)  