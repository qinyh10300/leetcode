#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# 使用**哈希**方法，如果数组为有序排列，也可以使用双指针方法

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, value in enumerate(nums):
            # print(target - nums[i], dict, (target - nums[i]) in dict)
            if (target - nums[i]) in dict:
                return dict[target - nums[i]], i
            else:
                dict[nums[i]] = i
# @lc code=end

