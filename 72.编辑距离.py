#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # # 记忆化搜索思路
        # @cache
        # def dfs(i, j):
        #     if i<0:  # 注意边界条件
        #         return j+1
        #     if j<0:  # 如果j<0 需要把另一个字符串都去掉
        #         return i+1
        #     if word1[i] == word2[j]:
        #         return dfs(i-1, j-1)
        #     return min(dfs(i, j-1), dfs(i-1, j), dfs(i-1, j-1)) + 1
        # return dfs(n-1, m-1)
        
        # # 递推
        # f = [[0] * (m+1) for _ in range(n+1)]
        # f[0] = [j for j in range(m+1)]
        # for i in range(n):
        #     f[i+1][0] = i+1
        #     for j in range(m):
        #         if word1[i] == word2[j]:
        #             f[i+1][j+1] = f[i][j]
        #         else:
        #             f[i+1][j+1] = min(f[i][j+1], f[i+1][j], f[i][j]) + 1
        # return f[n][m]
    
        # # 两个数组递推
        # f = [[0] * (m+1) for _ in range(2)]
        # f[0] = [j for j in range(m+1)]
        # for i in range(n):
        #     f[(i+1)%2][0] = i+1
        #     for j in range(m):
        #         if word1[i] == word2[j]:
        #             f[(i+1)%2][j+1] = f[i%2][j]
        #         else:
        #             f[(i+1)%2][j+1] = min(f[i%2][j+1], f[(i+1)%2][j], f[i%2][j]) + 1
        # return f[n%2][m]
    
        # **一个数组递推**
        f = [j for j in range(m+1)]
        for i in range(n):
            pre = f[0]
            f[0] = i+1
            for j in range(m):
                tmp = f[j+1]
                if word1[i] == word2[j]:
                    f[j+1] = pre
                else:
                    f[j+1] = min(f[j+1], f[j], pre) + 1
                pre = tmp
        return f[m]
# @lc code=end

