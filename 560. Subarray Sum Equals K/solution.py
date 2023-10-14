#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        sum_dict = defaultdict(int)
        sum_dict[0] = 1

        for num in nums:
            curr_sum += num
            count += sum_dict[curr_sum - k]
            sum_dict[curr_sum] += 1

        return count


# @lc code=end
