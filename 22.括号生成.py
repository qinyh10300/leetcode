#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # # 版本一
        # path = []
        # ans = []
        # def dfs(i, open, left):
        #     '''
        #     open为未闭合的左括号个数
        #     left为左括号个数
        #     '''
        #     if i == n*2:
        #         ans.append(''.join(path.copy()))
        #         return 
        #     if open > 0:
        #         path.append(")")
        #         dfs(i+1, open-1, left)
        #         path.pop()
        #     if left < n:
        #         path.append("(")
        #         left += 1
        #         dfs(i+1, open+1, left)
        #         path.pop()
        # dfs(0, 0, 0)
        # return ans

        # 版本二
        path = []
        ans = []
        def dfs(i, open):
            '''
            open为左括号个数
            '''
            if i == n*2:
                ans.append(''.join(path.copy()))
                return 
            if open > i-open:
                path.append(")")
                dfs(i+1, open)
                path.pop()
            if open < n:
                path.append("(")
                dfs(i+1, open+1)
                path.pop()
        dfs(0, 0)
        return ans
# @lc code=end

