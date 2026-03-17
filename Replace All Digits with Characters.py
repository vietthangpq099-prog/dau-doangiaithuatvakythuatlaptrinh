class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ket_qua = ""
        for i in range(len(s)):
            if i % 2 == 0:
                ket_qua = ket_qua + s[i]
            else:
                chu_cai_truoc = s[i-1]
                chu_so = int(s[i])
                ma_so_ascii = ord(chu_cai_truoc) + chu_so
                ky_tu_moi = chr(ma_so_ascii)
                ket_qua = ket_qua + ky_tu_moi
        return ket_qua 