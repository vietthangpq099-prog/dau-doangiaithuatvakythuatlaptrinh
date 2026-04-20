class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Tinh tong ky vong tu 0 den n bang cong thuc toan hoc
        tong_ky_vong = n * (n + 1) / 2
        
        # Tinh tong thuc te cua cac phan tu dang co trong mang
        tong_thuc_te = sum(nums)
        return tong_ky_vong - tong_thuc_te