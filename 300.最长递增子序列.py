#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 子集型回溯、记忆化搜索、递推、排序+去重+最长公共子序列 -> O(n^2)
        n = len(nums)
        # # 记忆化搜索思路
        # @cache
        # def dfs(i):
        #     # # i == 0时候，循环不会执行，自动return ans+1
        #     # if i < 0:
        #     #     return 0
        #     ans = 0
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             ans = max(ans, dfs(j))
        #     return ans + 1
        # return max(dfs(i) for i in range(n))
    
        # # 递推思路
        # f = [0] * (n)
        # for i in range(n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             f[i] = max(f[i], f[j])
        #     f[i] += 1
        # return max(f)

        # 贪心+二分查找 -> O(nlogn)
        # 类似单调栈？
        # 交换状态与状态值
        # f[i]表示末尾元素为nums[i]的LIS长度
        # g[i]表示长度为i+1的IS的末尾元素最小值
        g = [nums[0]]
        for i in range(1, n):
            if nums[i]>g[-1]:
                g.append(nums[i])
            else:
                # 这里的二分法寻找第一个大于等于target的值
                l = 0
                r = len(g)-1
                while l<=r:
                    mid = (l+r)//2
                    if nums[i] <= g[mid]:  # 注意这里
                        r = mid-1
                    else:
                        l = mid+1
                g[l] = nums[i]
        return len(g)
# @lc code=end

