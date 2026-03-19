class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        kc_tu_dau = 0
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                kc_tu_dau = i
                break
        kc_tu_cuoi = 0
        for i in range(n):
            if colors[i] != colors[n - 1]:
                kc_tu_cuoi = (n - 1) - i
                break
        if kc_tu_dau > kc_tu_cuoi:
            return kc_tu_dau
        else:
            return kc_tu_cuoi