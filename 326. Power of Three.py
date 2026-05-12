class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Cac so nho hon hoac bang 0 khong the la luy thua cua 3
        if n <= 0:
            return False  
        # Lien tuc chia 3 chung nao con chia het
        while n % 3 == 0:
            n /= 3
        # Neu cuoi cung giam ve dung 1 thi la True
        return n == 1