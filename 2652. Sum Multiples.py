class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        tong = 0
        
        # Duyet qua cac so tu 1 den n (bao gom ca n)
        for i in range(1, n + 1):
            # Kiem tra dieu kien chia het cho 3, 5 hoac 7
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                tong += i
                
        return tong