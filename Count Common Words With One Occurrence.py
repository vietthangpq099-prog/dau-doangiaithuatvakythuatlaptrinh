class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        dem1 = {}
        for tu in words1:
            if tu in dem1:
                dem1[tu] += 1
            else:
                dem1[tu] = 1
        dem2 = {}
        for tu in words2:
            if tu in dem2:
                dem2[tu] += 1
            else:
                dem2[tu] = 1
        ket_qua = 0
        for tu in dem1:
            if dem1[tu] == 1:
                if tu in dem2 and dem2[tu] == 1:
                    ket_qua += 1
        return ket_qua