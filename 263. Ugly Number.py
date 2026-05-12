class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # So xau xi phai la so nguyen duong
        if n <= 0:
            return False
            
        # Lan luot vat kiet cac uoc so 2, 3, va 5
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n /= factor
                
        # Neu phan loi con lai la 1, do la so xau xi hop le
        return n == 1