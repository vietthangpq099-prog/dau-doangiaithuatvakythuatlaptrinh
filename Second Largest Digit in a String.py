class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        lon_nhat = -1
        lon_thu_hai = -1
        for ky_tu in s:
            if ky_tu >= '0' and ky_tu <= '9':
                chu_so = int(ky_tu)
                if chu_so > lon_nhat:
                    lon_thu_hai = lon_nhat
                    lon_nhat = chu_so     
                elif chu_so < lon_nhat and chu_so > lon_thu_hai:
                    lon_thu_hai = chu_so 
        return lon_thu_hai