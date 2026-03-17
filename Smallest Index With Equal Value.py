class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for chi_so in range(len(nums)):
            phan_du = chi_so % 10
            if phan_du == nums[chi_so]:
                return chi_so
        return -1