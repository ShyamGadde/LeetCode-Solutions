#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        a, b = 2, 3
        for _ in range(4, n + 1):
            a, b = b, a + b
        return b
# @lc code=end

