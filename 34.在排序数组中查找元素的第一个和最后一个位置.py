#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
# 二分查找法，四种变式（>=, >, <=, <, 其实都是一种），三种写法（[], [), (], ()）

# @lc code=start
def find_lower_bound(nums: List[int], target: int) -> int:
    # 这里使用左右都是闭区间的写法
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:  # 区间不为空
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = find_lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:  # 特判
             return [-1, -1]
        end = find_lower_bound(nums, target+1) - 1
        return [start, end]
# @lc code=end

