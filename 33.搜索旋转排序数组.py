#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
# 可以先二分查找到最小值的位置（153题的方法），再判断target在哪个区间，再二分查找

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                if nums[mid] < target <= nums[-1]:   # 注意取不取等（corner case）
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[0] <= target <= nums[mid]:   # 注意取不取等（corner case）
                    right = mid - 1
                else:
                    left = mid + 1
        return left if nums[left] == target else -1
# @lc code=end

