class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        chu_so = sorted(str(num))

        so_thu_nhat = int(chu_so[0] + chu_so[2])
        so_thu_hai = int(chu_so[1] + chu_so[3])
        return so_thu_nhat + so_thu_hai