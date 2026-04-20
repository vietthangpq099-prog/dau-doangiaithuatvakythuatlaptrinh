class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
        
            tong = 0
            while n > 0:
                chu_so = n % 10
                tong += chu_so ** 2
                n //= 10 
            n = tong
        return n == 1