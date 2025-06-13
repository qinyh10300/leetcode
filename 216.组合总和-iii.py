#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(sum, last):  # 此代码有很多变种
            if len(path) == k or sum == n:
                if len(path) == k and sum == n:
                    ans.append(path.copy())
                return 
            rest = k - len(path) - 1
            for j in range(last+1, 10):
                if (j + j + rest) * (rest + 1) // 2 > n - sum:  # 剪枝
                    continue
                if (18 - rest) * (rest + 1) // 2 < n - sum - j:  # 剪枝
                    continue
                path.append(j)
                dfs(sum+j, j)
                path.pop()
        dfs(0, 0)
        return ans
# @lc code=end

