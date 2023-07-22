class Solution(object):
    # Approach 4: 
    # Runtime: Beats 89.56%of users with Python; Memory: Beats 30.70%of users with Python
    def searchRange(self, nums, target):
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
            
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]


if __name__ == "__main__":
    nums = [1]
    target = 1
    s = Solution()
    print(s.searchRange(nums, target))

"""
        # Approach 1:
        # Runtime: Beats 86.26%of users with Python; Memory: Beats 8.09%of users with Python
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        if len(res) == 0: 
            return [-1,-1]
        elif len(res) == 1:
            return [res[0], res[0]]
        return [res[0], res[-1]]
"""

"""
# Approach 2: 
# Runtime: Beats 74.05%of users with Python; Memory: Beats 58.82%of users with Python
def searchRange(self, nums, target):
    # when flag is True, find the first element 
    # when flag is Flase, find the last element

    return [findTarget(nums, target, True), findTarget(nums, target, False)]


def findTarget(nums, target, flag):
# Left snd right pointers
left, right = 0, len(nums) - 1
# Index of first occurrence
result = -1
# Loop until the two pointers meet
while left <= right:
    # Middle index
    middle = left + (right - left) // 2
    # Check if we have found the value
    if target == nums[middle]:
        result = middle
        if flag: 
            right = middle - 1
        else:
            left = middle + 1
    # If the target is less than the element
    # at the middle index
    elif target < nums[middle]:
        right = middle - 1
    # If the target is greater than the element
    # at the middle index
    else:
        left = middle + 1
return result
"""

"""
# Approach 3: 
Runtime: Beats 36.53%of users with Python; Memory: Beats 18.22%of users with Python\
 def searchRange(self, nums, target):
    first_last = [-1, -1]
    for i in range(len(nums)):
        if nums[i] == target:
            if first_last[0] == -1:
                first_last[0] = i
            first_last[1] = i
    return first_last
"""