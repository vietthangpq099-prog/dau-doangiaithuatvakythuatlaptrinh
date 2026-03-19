class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ky_luc = 0
        for cau in sentences:
            so_tu = len(cau.split(" "))
            if so_tu > ky_luc:
                ky_luc = so_tu
        return ky_luc
        