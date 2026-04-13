class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left = 1
        right = x // 2
        while left <= right:
            mid = left + (right - left) // 2
            
            binh_phuong = mid * mid
            if binh_phuong == x:
                return mid
            elif binh_phuong < x:
                # Neu binh phuong nho hon x, dap an nam o nua phai
                left = mid + 1
            else:
                # Neu binh phuong lon hon x, dap an nam o nua trai
                right = mid - 1
        return right