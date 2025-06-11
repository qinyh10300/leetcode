#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
# 直接寻找最大值是一个非常取巧的方法（脑际急转弯），但是复杂度O(n)
# 二分法，复杂度O(logn)
# 看到题的第一直觉，“居然可以用二分法！”
# 俗话说「人往高处走，水往低处流」。如果我们从一个位置开始，不断地向高处走，那么最终一定可以到达一个峰值位置。

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            if mid+1 < n and nums[mid] < nums[mid+1]:  # 判断数组越界的情况
                left = mid + 1
            else:
                right = mid - 1
        return left
# @lc code=end

