#
# @lc app=leetcode.cn id=1039 lang=python3
#
# [1039] 多边形三角剖分的最低得分
#

# @lc code=start
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        # # 记忆化搜索  O(n^3)
        # @cache
        # def dfs(i, j):
        #     if i == j-1:
        #         return 0
        #     ans = inf
        #     for k in range(i+1, j):
        #         ans = min(ans, dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k])
        #     return ans
        # return dfs(0, n-1)
    
        # 递推  O(n^3)
        f = [[0] * n for _ in range(n)]
        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                ans = inf
                for k in range(i+1, j):
                    ans = min(ans, f[i][k] + f[k][j] + values[i] * values[j] * values[k])
                f[i][j] = ans
        return f[0][n-1]
# @lc code=end

