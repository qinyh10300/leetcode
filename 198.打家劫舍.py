#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
# 记忆化搜索、递推、动态规划

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动态规划：状态定义、状态转移方程
        
        # # 方法一：递推1
        # n = len(nums)
        # f = [0] * n
        # f[0] = nums[0]
        # for i in range(1, n):
        #     f[i] = max(f[i-1], f[i-2]+ nums[i])  # python数组的f[-1]也有定义，是数组最后一个值
        # return f[n-1]

        # # 方法二：递推2
        # f1 = 0
        # f2 = nums[0]
        # for i in range(1, len(nums)):
        #     tmp = max(f2, f1+ nums[i])
        #     f1 = f2
        #     f2 = tmp
        # return f2

        # # 方法三：暴力搜索无剪枝
        # n = len(nums)
        # ans = 0
        # def dfs(i, path):
        #     nonlocal ans
        #     if i >= n:
        #         ans = max(ans, path)
        #         return
        #     dfs(i+1, path)
        #     dfs(i+2, path+nums[i])
        # dfs(0, 0)
        # return ans

        # 方法四：记忆化搜索
        n = len(nums)
        cache = [-1] * n
        def dfs(i):
            if i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]
            res = max(dfs(i-2)+nums[i], dfs(i-1))
            cache[i] = res
            return res
        return dfs(n-1)
# @lc code=end

