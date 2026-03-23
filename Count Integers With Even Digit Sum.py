class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        dem = 0
        for i in range(1, num + 1):
            tong_chu_so = 0
            so_tam = i
            while so_tam > 0:
                tong_chu_so += so_tam % 10
                so_tam //= 10
            if tong_chu_so % 2 == 0:
                dem += 1 
        return dem