class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
    # Dieu kien 1: n > 0 (So duong)
    # Dieu kien 2: n & (n - 1) == 0 (La luy thua cua 2, chi co dung 1 bit 1)
    # Dieu kien 3: n & 0xAAAAAAAA == 0 (Bit 1 khong nam o vi tri le -> nam o vi tri chan)
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0