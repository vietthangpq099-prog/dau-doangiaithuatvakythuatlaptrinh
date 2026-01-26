class Solution(object):
    def findNumbers(self, nums):
        dem = 0
        for so in nums:
            chuoi_so = str(so)
            so_luong_chu_so = len(chuoi_so)
            if so_luong_chu_so % 2 == 0:
                dem += 1
        return dem