#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # # 方法一：枚举每个元素选与不选
        # n = len(nums)
        # ans = []
        # path = []
        # def dfs(i):
        #     if i == n:
        #         ans.append(path.copy())
        #         return
        #     dfs(i+1)  # 不选当前这个元素
        #     path.append(nums[i])
        #     dfs(i+1)  # 选当前这个元素
        #     path.pop()
        # dfs(0)
        # return ans

        # 方法二：枚举子集的下一个元素选哪个
        n = len(nums)
        ans = []
        path = []
        def dfs(i):
            ans.append(path.copy())
            for j in range(i, n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return ans
# @lc code=end

