# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            ket_qua_doan = guess(mid)
            if ket_qua_doan == 0:
                return mid
            # Số đoán lớn hơn số bí mật, tìm nửa trái
            elif ket_qua_doan == -1:
                right = mid - 1
            # Số đoán nhỏ hơn số bí mật , tìm nửa phải
            else:
                left = mid + 1
        