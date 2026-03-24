class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        tap_hop_nums = set(nums)
        while original in tap_hop_nums:
            original *= 2
        return original
        