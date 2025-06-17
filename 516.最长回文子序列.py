#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 方法一：求s和翻转后的s的最长公共子序列  O(n^2)
        n = len(s)
        # # 记忆化搜索思路  O(n^2)
        # @cache
        # def dfs(i, j):
        #     if i >= j:
        #         return 1 if i == j else 0
        #     if s[i] == s[j]:
        #         return dfs(i+1, j-1)+2
        #     return max(dfs(i+1, j), dfs(i, j-1))
        # return dfs(0, n-1)
        # 记忆化搜索思路  O(n^2)
        f = [[0] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = 1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i+1][j-1] + 2
                else:
                    f[i][j] = max(f[i+1][j], f[i][j-1])

        return f[0][n-1]
# @lc code=end

