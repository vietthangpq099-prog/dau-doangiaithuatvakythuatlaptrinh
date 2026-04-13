# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            # Neu mid bi loi
            if isBadVersion(mid):
                # Phien ban loi dau tien co the chinh la mid hoac nam o nua trai
                right = mid
            else:
                # Neu mid tot, phien ban loi dau tien chac chan nam o nua phai (sau mid)
                left = mid + 1
        return left