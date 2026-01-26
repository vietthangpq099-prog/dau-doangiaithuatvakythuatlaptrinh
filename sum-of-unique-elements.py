class Solution(object):
    def sumOfUnique(self, nums):
        tong = 0
        for so in nums:
            so_lan_xuat_hien = nums.count(so)

            if so_lan_xuat_hien == 1:
                tong += so
        return tong