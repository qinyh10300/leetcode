#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 方法一：枚举每个逗号放的位置（枚举每个位置的逗号选与不选）
        n = len(s)
        ans = []
        path = []
        last = 0
        def dfs(i):  # 也可以在函数参数里面记录last
            nonlocal last
            if i == n:
                t = s[last: i]
                if t == t[::-1]:
                    path.append(t)
                    ans.append(path.copy())
                    path.pop()
                return
            dfs(i+1)  # 不选当前这个元素
            t = s[last: i]
            if t == t[::-1]:
                path.append(t)
                tmp = last
                last = i
                dfs(i+1)  # 选当前这个元素
                last = tmp  # 恢复现场
                path.pop()
        dfs(1)
        return ans

        # # 方法二：枚举子集的下一个逗号放在哪里（枚举每个字串结束的位置）
        # n = len(s)
        # ans = []
        # path = []
        # def dfs(i):
        #     if i == n:
        #         ans.append(path.copy())
        #         return
        #     for j in range(i, n):  # 注意边界条件
        #         t = s[i:j+1]
        #         if t == t[::-1]:
        #             path.append(t)
        #             dfs(j+1)
        #             path.pop()
        # dfs(0)
        # return ans
# @lc code=end

