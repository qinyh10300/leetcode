#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        # # 记忆化搜索思路
        # @cache
        # def dfs(i, hold):
        #     if i < 0:
        #         return 0 if hold == 0 else -inf
        #     if hold:
        #         return max(dfs(i-1, 0) - prices[i], dfs(i-1, hold))
        #     else:
        #         return max(dfs(i-1, 1) + prices[i], dfs(i-1, hold))
            
        # return dfs(n-1, 0)

        # # 递推思路
        # f = [[0, 0] for i in range(n+1)]
        # f[0][1] = -inf
        # for i in range(n):
        #     f[i+1][0] = max(f[i][0], f[i][1] + prices[i])
        #     f[i+1][1] = max(f[i][1], f[i][0] - prices[i])
            
        # return f[n][0]

        # 使用两个变量表示的递推思路
        f0 = 0
        f1 = -inf
        for i in range(n):
            new_f0 = max(f0, f1 + prices[i])
            new_f1 = max(f1, f0 - prices[i])
            f1 = new_f1
            f0 = new_f0
            
        return f0
            
# @lc code=end

