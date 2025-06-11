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

        # 相向双指针方法
        n = len(height)
        left = 0
        right = n-1
        ans = 0
        max_pre = 0
        max_suf = 0 
        while left < right:
            max_pre = max(max_pre, height[left])
            max_suf = max(max_suf, height[right])
            if max_pre > max_suf:
                ans += max_suf - height[right]
                right -= 1
            else:
                ans += max_pre - height[left]
                left += 1
        return ans

        
# @lc code=end

