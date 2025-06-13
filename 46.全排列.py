#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # # 写法一
        # ans = []
        # path = []
        # n = len(nums)
        # on_path = [0] * n
        # def dfs(i):
        #     if i == n:
        #         ans.append(path.copy())
        #         return
        #     for j in range(0, n):
        #         if not on_path[j]:
        #             path.append(nums[j])
        #             on_path[j] = 1
        #             dfs(i+1)
        #             on_path[j] = 0
        #             path.pop()
        # dfs(0)
        # return ans
    
        # 写法一，利用数据结构set（集合）
        ans = []
        path = []
        n = len(nums)
        def dfs(i, s):
            if i == n:
                ans.append(path.copy())
                return
            for j in s:
                path.append(j)
                dfs(i+1, s-{j})
                path.pop()
        dfs(0, set(nums))
        return ans
# @lc code=end

