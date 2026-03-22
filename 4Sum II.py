class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        dem_tong = {}
        ket_qua = 0
        
        for so1 in nums1:
            for so2 in nums2:
                tong = so1 + so2
                if tong in dem_tong:
                    dem_tong[tong] += 1
                else:
                    dem_tong[tong] = 1
        for so3 in nums3:
            for so4 in nums4:
                phan_bu = -(so3 + so4)
                if phan_bu in dem_tong:
                    ket_qua += dem_tong[phan_bu]
                
        return ket_qua