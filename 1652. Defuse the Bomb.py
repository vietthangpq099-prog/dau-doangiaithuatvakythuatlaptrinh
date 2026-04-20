class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        result = [0] * n
    
        if k == 0:
            return result
        for i in range(n):
            tong = 0
            if k > 0:
                for j in range(1, k + 1):
                    tong += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    tong += code[(i - j) % n]
            result[i] = tong
        return result