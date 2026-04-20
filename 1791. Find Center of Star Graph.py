class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        u1, v1 = edges[0]
        u2, v2 = edges[1]
        # Kiem tra xem u1 co nam trong canh thu 2 hay khong
        if u1 == u2 or u1 == v2:
            return u1
        return v1