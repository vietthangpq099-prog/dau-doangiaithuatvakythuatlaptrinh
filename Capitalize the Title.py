class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        cac_tu = title.split()
        ket_qua = []
        for tu in cac_tu:
            # Nếu từ ngắn (1 hoặc 2 ký tự)
            if len(tu) <= 2:
                ket_qua.append(tu.lower())
            # Nếu từ dài (3 ký tự trở lên)
            else:
                ket_qua.append(tu.capitalize())
        return " ".join(ket_qua)