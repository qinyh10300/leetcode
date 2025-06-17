#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
# 经典相向双指针问题

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # # 前后缀方法
        # n = len(height)
        # pre_max = [0] * n
        # suf_max = [0] * n
        # pre_max[0] = height[0]
        # suf_max[n-1] = height[n-1]
        # for i in range(1, n):
        #     pre_max[i] = max(pre_max[i-1], height[i])
        #     suf_max[n-i-1] = max(suf_max[n-i], height[n-i-1])
        # ans = 0
        # for i in range(n):
        #     ans += min(pre_max[i], suf_max[i])-height[i]
        # return ans

        # # 相向双指针方法
        # n = len(height)
        # left = 0
        # right = n-1
        # ans = 0
        # max_pre = 0
        # max_suf = 0 
        # while left < right:
        #     max_pre = max(max_pre, height[left])
        #     max_suf = max(max_suf, height[right])
        #     if max_pre > max_suf:
        #         ans += max_suf - height[right]
        #         right -= 1
        #     else:
        #         ans += max_pre - height[left]
        #         left += 1
        # return ans

        # # 单调栈思路（版本一：自己实现的比较麻烦）
        # ans = 0
        # st = []
        # n = len(height)
        # for i in range(n):
        #     last_height = 0
        #     while st and height[i] > height[st[-1]]:
        #         ans += (i - st[-1] - 1) * (height[st[-1]] - last_height)
        #         last_height = height[st[-1]]
        #         st.pop()
        #     if st:
        #         ans += (i - st[-1] - 1) * (height[i] - last_height)
        #         if height[i] == height[st[-1]]:
        #             st.pop()
        #         st.append(i)
        #     else:
        #         st.append(i)
        # return ans
    
        # 单调栈思路（版本二：官方版本）
        ans = 0
        st = []
        n = len(height)
        for i in range(n):
            while st and height[i] > height[st[-1]]:
                bottom_height = height[st.pop()]
                if len(st) == 0:
                    break
                ans += (min(height[st[-1]], height[i])- bottom_height) * (i - st[-1] - 1)
            st.append(i)
        return ans
        
# @lc code=end

