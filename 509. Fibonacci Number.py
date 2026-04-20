class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        a = 0  # Tuong duong F(n-2)
        b = 1  # Tuong duong F(n-1)
        for i in range(2, n + 1):
            # So moi bang tong 2 so cu
            c = a + b
            a = b
            b = c
        return b