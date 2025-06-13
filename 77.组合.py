#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            if len(path) == k:
                ans.append(path.copy())
                return 
            if k - len(path) > n - i:  # 剪枝
                return 
            for j in range(i+1, n+1):
                path.append(j)
                dfs(j)
                path.pop()
        dfs(0)
        return ans
# @lc code=end

