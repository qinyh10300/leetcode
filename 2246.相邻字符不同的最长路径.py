#
# @lc app=leetcode.cn id=2246 lang=python3
#
# [2246] 相邻字符不同的最长路径
#

# @lc code=start
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # # 写法一
        # n = len(parent)
        # ch = [[] for _ in range(n)]
        # for i in range(1, n):
        #     ch[parent[i]].append(i)
        
        # ans = 1  # 至少有一个节点
        # def dfs(i):
        #     max1 = 0
        #     max2 = 0
        #     for j in ch[i]:
        #         length = dfs(j)
        #         if s[j] != s[i]:
        #             # 更新最大值和次大值的时候，要注意！（找了好久这个bug）
        #             if length > max1:
        #                 max1, max2 = length, max1
        #             else:
        #                 max2 = max(max2, length)
        #         nonlocal ans
        #         ans = max(ans, max1 + max2 + 1)
        #     return max1 + 1
        # dfs(0)
        # return ans

        n = len(parent)
        ch = [[] for _ in range(n)]
        for i in range(1, n):
            ch[parent[i]].append(i)
        
        ans = 1  # 至少有一个节点
        def dfs(i):
            max1 = 0
            for j in ch[i]:
                length = dfs(j)
                if s[j] != s[i]:
                    nonlocal ans
                    ans = max(ans, max1 + length + 1)
                    if length > max1:
                        max1 = length
            return max1 + 1
        dfs(0)
        return ans

# @lc code=end

