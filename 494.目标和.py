#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
# 0-1背包问题的实现

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
        return max(dfs(i-1, c), dfs(i-1, c-w[i]) + v[i])
    
    return dfs(n-1, capacity)

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # p为所有正数之和
        # s-p为所有负数之和，s为所有数之和
        # p - (s-p) = 2p - s = target
        # p = (target + s) / 2
        target += sum(nums)
        if target < 0 or target % 2 == 1:
            return 0
        
        target //= 2
        n = len(nums)

        # # 记忆化搜索
        # @cache  
        # def dfs(i ,c):
        #     # 这种方式更保险
        #     if i < 0:
        #          return 1 if c == 0 else 0
        #     # # 下面这种有一点问题，没有考虑w[i]=0的情况
        #     # if c == 0:
        #     #     return 1
        #     # if i < 0:
        #     #     return 0
        #     if c < nums[i]:
        #         return dfs(i-1, c)
        #     return dfs(i-1, c) + dfs(i-1, c-nums[i])
        
        # return dfs(n-1, target)

        # # 递推
        # f = [[0] * (target+1) for _ in range(n+1)] # 第一个维度平移一位
        # f[0][0] = 1

        # for i, x in enumerate(nums):
        #     for c in range(target+1):
        #         if c < x:
        #             f[i+1][c] = f[i][c]
        #         else:
        #             f[i+1][c] = f[i][c] + f[i][c-x]
        # # 这里的x对应 nums[i] ，但因为 i 平移了一位，所以对应关系是正确的。
        
        # return f[n][target]

        # # 两个数组递推
        # f = [[0] * (target+1) for _ in range(2)]
        # f[0][0] = 1
        # for i, x in enumerate(nums):
        #     for c in range(target+1):
        #         if c<x:
        #             f[(i+1)%2][c] = f[i%2][c]
        #         else:
        #             f[(i+1)%2][c] = f[i%2][c] + f[i%2][c-x]

        # return f[n%2][c]

        # 一个数组递推
        f = [0] * (target+1)
        f[0] = 1
        for i, x in enumerate(nums):
            for c in range(target, -1, -1):  # 逆序更新
                # if c < x:
                #     f[c] = f[c]
                # else:
                #     f[c] = f[c] + f[c-x]
                if c >= x:
                    f[c] = f[c] + f[c-x]

        return f[target]
    
        '''
        如果是至多为target，应该改成
    
        # 递推
        def dfs(i ,c):
            if i < 0:
                 return 1
            if c < nums[i]:
                return dfs(i-1, c)
            return dfs(i-1, c) + dfs(i-1, c-nums[i])

        # 一个数组递推
        f = [1] * (target+1)
        for i, x in enumerate(nums):
            for c in range(target, -1, -1):  # 逆序更新
                if c >= x:
                    f[c] = f[c] + f[c-x]
        '''

            
        '''
        如果是至少为target，应该改成
    
        # 递推
        def dfs(i ,c):
            if i < 0:
                 return 1 if c <= 0 else 0
            return dfs(i-1, c) + dfs(i-1, c-nums[i])

        # 一个数组递推
        f = [0] * (target+1)
        f[0] = 1
        for i, x in enumerate(nums):
            for c in range(target, -1, -1):  # 逆序更新
                if c >= x:
                    f[c] = f[c] + f[min(c-x, 0)]
        '''


# @lc code=end

