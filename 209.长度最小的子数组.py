#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
# 同向双指针 -> 滑动窗口

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # n = len(nums)
        # left = 0
        # right = 0
        # ans = n+1
        # # 优化如下：
        # sum = nums[0]
        # while left <= right:
        #     if sum < target:
        #         right += 1
        #         if right > n-1:
        #             break
        #         sum += nums[right]
        #     else:
        #         ans = min(ans, right - left + 1)
        #         sum -= nums[left]
        #         left += 1
        # return ans if ans < n+1 else 0

        # 更简洁、经典的写法如下：
        n = len(nums)
        left = 0
        right = 0
        ans = n+1
        sum = 0
        for right, value in enumerate(nums):
            sum += value
            while sum >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
        return ans if ans < n+1 else 0
# @lc code=end

