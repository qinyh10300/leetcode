#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # # 记忆化搜索思路
        # @cache
        # def dfs(i, hold):
        #     if i<0:
        #         return -inf if hold else 0
        #     if hold:
        #         return max(dfs(i-1, hold), dfs(i-2, 0) - prices[i])
        #     return max(dfs(i-1, hold), dfs(i-1, 1) + prices[i])
        
        # return dfs(n-1, 0)

        # # 递推思路
        # f = [[0, 0] for _ in range(n+1)]
        # f[0][1] = -inf
        # for i in range(n):
        #     f[i+1][0] = max(f[i][0], f[i][1] + prices[i])
        #     f[i+1][1] = max(f[i][1], f[max(0, i-1)][0] - prices[i])
        
        # return f[n][0]
    
        # 递推思路（利用滚动数组，再次降低空间复杂度）
        f = [[0, 0] for _ in range(2)]
        f[0][1] = -inf
        for i in range(n):
            f[(i+1)%2][1] = max(f[i%2][1], f[(max(0, i-1))%2][0] - prices[i])
            f[(i+1)%2][0] = max(f[i%2][0], f[i%2][1] + prices[i])
        
        return f[n%2][0]
# @lc code=end

