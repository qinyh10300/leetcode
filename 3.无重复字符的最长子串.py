#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
# hashmap + 滑动窗口（双指针）

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left = 0
        # ans = 0
        # hashmap = Counter()
        # for right, value in enumerate(s):
        #     if hashmap[value] == 0:
        #         print(left, right)
        #         ans = max(ans, right - left + 1)
        #     else:
        #         while hashmap[value] != 0:
        #             hashmap[s[left]] -= 1
        #             left += 1
        #     hashmap[value] += 1
        # return ans 

        # 更标准的写法
        left = 0
        ans = 0
        hashmap = Counter()
        for right, value in enumerate(s):
            hashmap[value] += 1
            while hashmap[value] > 1:
                hashmap[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans 
# @lc code=end

