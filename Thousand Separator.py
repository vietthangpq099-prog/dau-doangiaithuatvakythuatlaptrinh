class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return "0"
            
        ket_qua = ""
        dem = 0
        while n > 0:
            chu_so = n % 10 
            ket_qua = str(chu_so) + ket_qua 
            dem += 1
            n = n // 10 
            if dem == 3 and n > 0:
                ket_qua = "." + ket_qua
                dem = 0 
        return ket_qua