#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2) 
        # # 记忆化搜索思路
        # @cache
        # def dfs(i, j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return dfs(i-1, j-1) + 1
        #     else:
        #         return max(dfs(i, j-1), dfs(i-1, j))
        # return dfs(n-1, m-1)
    
        # # 递推
        # f = [[0] * (m+1) for _ in range(n+1)]
        # for i in range(n):
        #     for j in range(m):
        #         if text1[i] == text2[j]:
        #             f[i+1][j+1] = f[i][j] + 1
        #         else:
        #             f[i+1][j+1] = max(f[i+1][j], f[i][j+1])
        # return f[n][m]
    
        # # 两个数组递推
        # f = [[0] * (m+1) for _ in range(2)]
        # for i in range(n):
        #     for j in range(m):
        #         if text1[i] == text2[j]:
        #             f[(i+1)%2][j+1] = f[i%2][j] + 1
        #         else:
        #             f[(i+1)%2][j+1] = max(f[(i+1)%2][j], f[i%2][j+1])
        # return f[n%2][m]
    
        # **一个数组递推**
        f = [0] * (m+1)
        for i in range(n):
            pre = f[0]   # 储存左上方临时值
            for j in range(m):
                tmp = f[j+1]
                if text1[i] == text2[j]:
                    f[j+1] = pre + 1
                else:
                    f[j+1] = max(f[j], f[j+1])
                pre = tmp
        return f[m]
# @lc code=end

