class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []

        def dfs(n, path, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(n+1, len(candidates)):
                if i > n+1 and candidates[i] == candidates[i-1]:
                    continue
                dfs(i, path+[candidates[i]], target-candidates[i])
        dfs(-1, [], target)
        return res
    

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8 
    s = Solution()
    print(s.combinationSum2(candidates, target)) 