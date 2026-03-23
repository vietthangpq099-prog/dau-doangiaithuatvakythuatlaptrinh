class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mang_rut_gon = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                mang_rut_gon.append(nums[i])
        dem = 0
        # Chạy từ phần tử thứ 2 đến phần tử áp chót
        for i in range(1, len(mang_rut_gon) - 1):
            so_trai = mang_rut_gon[i - 1]
            so_hien_tai = mang_rut_gon[i]
            so_phai = mang_rut_gon[i + 1]
    
            if so_hien_tai > so_trai and so_hien_tai > so_phai:
                dem += 1
            elif so_hien_tai < so_trai and so_hien_tai < so_phai:
                dem += 1
        return dem