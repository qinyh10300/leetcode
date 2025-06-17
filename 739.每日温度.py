#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # 从右到左
        # n = len(temperatures)
        # ans = [0] * n
        # st = []
        # for i in range(n-1, -1, -1):
        #     t = temperatures[i]
        #     while st and t >= temperatures[st[-1]]:
        #         st.pop()
        #     if st:
        #         ans[i] = st[-1] - i
        #     else:
        #         ans[i] = 0
        #     st.append(i)
        # return ans
    
        # 从右到左
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n):
            t = temperatures[i]
            while st and t > temperatures[st[-1]]:
                index = st.pop()
                ans[index] = i - index
            st.append(i)
        return ans
# @lc code=end

