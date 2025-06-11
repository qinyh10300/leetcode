#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # hashmap 写法
        # dict = {}
        # for i, value in enumerate(numbers):
        #     if target - value in dict:
        #         return dict[target - value]+1, i+1
        #     else:
        #         dict[value] = i

        # 双指针 写法（利用了有序排列这一性质）
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return left+1, right+1
# @lc code=end

