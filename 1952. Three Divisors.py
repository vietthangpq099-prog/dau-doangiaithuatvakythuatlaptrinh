class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        
        # Duyet tu 1 den n de tim uoc so
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
            # Toi uu thoat som: Neu co nhieu hon 3 uoc so thi chac chan la False
            if count > 3:
                return False
        # Tra ve True neu co chinh xac 3 uoc so
        return count == 3