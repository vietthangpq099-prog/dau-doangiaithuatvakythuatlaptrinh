class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        quota = len(candyType) // 2
        so_vi_keo = len(set(candyType))
        return min(quota, so_vi_keo)