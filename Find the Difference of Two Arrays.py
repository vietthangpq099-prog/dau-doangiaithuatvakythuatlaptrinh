class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        tap_1 = set(nums1)
        tap_2 = set(nums2)
        chi_co_o_1 = list(tap_1 - tap_2)
        chi_co_o_2 = list(tap_2 - tap_1)
        return [chi_co_o_1, chi_co_o_2]