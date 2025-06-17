#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列写法（单调队列和单调栈往往不直接存放单调的值，而是存放单调的值对应的下标）
        q = deque()
        n = len(nums)
        ans = []
        for i in range(n):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i-q[0]+1 > k:  # 判断队首是否移出窗口
                q.popleft()
            if i >= k-1:
                ans.append(nums[q[0]])
        return ans
# @lc code=end

