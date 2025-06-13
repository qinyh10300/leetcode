#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n
        def dfs(i):
            if i == n:
                ans.append(''.join(path.copy()))  # 这里必须有.copy()，不然到最后值会改变。列表是引用传递
                return
            # for j in range(len(MAPPING[int(digits[i])])):
            #     path[i] = MAPPING[int(digits[i])][j]
            #     dfs(i+1)
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        dfs(0)
        return ans
# @lc code=end

