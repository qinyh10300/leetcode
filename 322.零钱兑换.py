#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
# 完全背包问题

# capacity: 背包容量
# w[i]: 第 i 个物品的体积
# c[i]: 第 i 个物品的价值
# 返回：所选物品体积和不超过 capacity 的前提下，所能得到的最大价值和
def zero_one_knapsack(capacity: int, w: List[int], v: List[int]) -> int:
    n = len(w)  # n个物品

    @cache   # 这个装饰器用于记忆化搜索
    def dfs(i, c):
        if i < 0:
            return 0
        if c < w[i]:
            return dfs(i-1, c)
        return max(dfs(i-1, c), dfs(i, c-w[i]) + v[i])
    
    return dfs(n-1, capacity)

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # # 记忆化搜索思路
        # @cache
        # def dfs(i, c):
        #     if i<0:
        #         return 0 if c == 0 else inf
        #     if c < coins[i]:
        #         return dfs(i-1, c)
        #     return min(dfs(i-1, c), dfs(i, c-coins[i])+1)
        
        # ans = dfs(n-1, amount)
        # return ans if ans < inf else -1
    
        # # 递推
        # f = [[inf] * (amount + 1) for _ in range(n+1)]
        # f[0][0] = 0
        # for i, x in enumerate(coins):
        #     for c in range(amount+1):
        #         if c < x:
        #             f[i+1][c] = f[i][c]
        #         else:
        #             f[i+1][c] = min(f[i][c], f[i+1][c-x]+1)
        # return f[n][amount] if f[n][amount] < inf else -1
    
        # # 两个数组递推
        # f = [[inf] * (amount + 1) for _ in range(2)]
        # f[0][0] = 0
        # for i, x in enumerate(coins):
        #     for c in range(amount+1):
        #         if c < x:
        #             f[(i+1)%2][c] = f[i%2][c]
        #         else:
        #             f[(i+1)%2][c] = min(f[i%2][c], f[(i+1)%2][c-x]+1)
        # return f[n%2][amount] if f[n%2][amount] < inf else -1
    
        # 一个数组递推
        f = [inf] * (amount + 1)
        f[0] = 0
        for i, x in enumerate(coins):
            for c in range(amount+1):
                if c >= x:
                    f[c] = min(f[c], f[c-x]+1)
        return f[amount] if f[amount] < inf else -1

# @lc code=end

