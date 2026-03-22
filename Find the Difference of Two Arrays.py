class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        tap_1 = set(nums1)
        tap_2 = set(nums2)
        
        chi_co_o_1 = []
        for so in tap_1:
            if so not in tap_2:
                chi_co_o_1.append(so)
        chi_co_o_2 = []
        for so in tap_2:
            if so not in tap_1:
                chi_co_o_2.append(so)
        return [chi_co_o_1, chi_co_o_2]