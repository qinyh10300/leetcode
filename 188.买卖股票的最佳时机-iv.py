#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # # 记忆化搜索思路
        # @cache
        # def dfs(i, j, hold):
        #     if j < 0:
        #         return -inf
        #     if i < 0:
        #         return -inf if hold else 0
        #     if hold:
        #         return max(dfs(i-1, j, hold), dfs(i-1, j, 0) - prices[i])
        #     return max(dfs(i-1, j, hold), dfs(i-1, j-1, 1) + prices[i])
        
        # return dfs(n-1, k, 0)

        # # 递推思路
        # f = [[[0, 0] for j in range(k+2)] for i in range(n+1)]
        # f[0] = [[0, -inf] for j in range(k+2)]
        # for i in range(n):
        #     f[i][0] = [-inf, -inf]
        #     for j in range(k+1):
        #         f[i+1][j+1][1] = max(f[i][j+1][1], f[i][j+1][0] - prices[i])
        #         f[i+1][j+1][0] = max(f[i][j+1][0], f[i][j][1] + prices[i])
        
        # return f[n][k+1][0]

        # 递推思路+空间优化
        f = [[0, -inf] for j in range(k+2)]
        for i in range(n):
            f[0] = [-inf, -inf]
            for j in range(k, -1, -1):
                f[j+1][1] = max(f[j+1][1], f[j+1][0] - prices[i])
                f[j+1][0] = max(f[j+1][0], f[j][1] + prices[i])
        
        return f[k+1][0]
# @lc code=end

