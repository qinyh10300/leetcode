#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 最多O(n^2)的算法
        # 枚举第一个数字，剩下两个数转化成两数之和问题（hashmap或者双指针）

        # # hashmap方法，但是有两个样例超出时间
        # n = len(nums)
        # ans = []
        # for i in range(n-2):
        #     target = -nums[i]
        #     dict = {}
        #     for j in range(i+1, n):
        #         if target - nums[j] in dict:
        #             _ans = [nums[i], nums[j], target - nums[j]]
        #             _ans.sort()  # 手动去重，可能比较慢
        #             if _ans not in ans:  # O(n)
        #                 ans.append(_ans)
        #         else:
        #             dict[nums[j]] = 1
        # return ans

        # 排序 + 双指针方法（推荐使用方法）
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
            target = -nums[i]
            left = i+1
            right = n-1
            while left < right:
                if nums[left] + nums[right] < target:
                    # 注释掉居然更快了
                    # while left < right and nums[left+1] == nums[left]:
                    #     left += 1
                    left += 1
                elif nums[left] + nums[right] > target:
                    # 注释掉居然更快了
                    # while left < right and nums[right-1] == nums[right]:
                    #     right -= 1
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    right -= 1
        return ans
    
        # # 排序 + hashmap
        # nums.sort()
        # n = len(nums)
        # ans = []
        # for i in range(n-2):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     if nums[i] + nums[i+1] + nums[i+2] > 0:
        #         break
        #     if nums[i] + nums[n-2] + nums[n-1] < 0:
        #         continue
        #     target = -nums[i]
        #     dict = {}
        #     flag = 0
        #     for j in range(i+1, n):
        #         if j > i+1 and nums[j] == nums[j-1]:
        #             if nums[j]*2 == target and flag == 0:
        #                 _ans = [nums[i], nums[j], nums[j-1]]
        #                 ans.append(_ans)
        #                 flag = 1
        #             continue
        #         if target - nums[j] in dict:
        #             _ans = [nums[i], nums[j], target - nums[j]]
        #             ans.append(_ans)
        #         else:
        #             dict[nums[j]] = 1
        # return ans
# @lc code=end

