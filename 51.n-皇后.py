#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        path = []
        diag1 = [0] * n * 2
        diag2 = [0] * n * 2
        def dfs(i, s):
            if i == n:
                ans.append(["." * k + "Q" + "." * (n-k-1) for k in path])
                return
            for j in s:
                if diag1[j+i] == 0 and diag2[j-i] == 0:
                    diag1[j+i] = 1
                    diag2[j-i] = 1
                    path.append(j)
                    dfs(i+1, s-{j})
                    path.pop()
                    diag1[j+i] = 0
                    diag2[j-i] = 0
        dfs(0, set(i for i in range(n)))
        return ans
# @lc code=end

