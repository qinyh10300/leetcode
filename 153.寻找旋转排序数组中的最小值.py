#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # # 下面是左右都是闭区间的写法，虽然也能work，但是还是不够简洁
        # n = len(nums)
        # left = 0
        # right = n-1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] >= nums[left]:
        #         if nums[mid] <= nums[right]:
        #             return nums[left]
        #         left = mid
        #     else:
        #         right = mid
        #     if right == left + 1:
        #         return nums[right]

        # # 左右都是闭区间的version2，非常简洁
        # n = len(nums)
        # left = 0
        # right = n-1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] <= nums[-1]:  # 这个<=号不能写成<号，写成<号就没法判断[3,4,5,1]这种情况（边界情况 corner case）
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return nums[left]

        # 下面是左右都是开区间的写法，非常简洁
        n = len(nums)
        left = -1
        right = n
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid
        return nums[right]
# @lc code=end

