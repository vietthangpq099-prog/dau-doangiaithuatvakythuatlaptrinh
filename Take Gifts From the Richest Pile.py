class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for _ in range(k):
            vi_tri_max = 0
            for i in range(len(gifts)):
                if gifts[i] > gifts[vi_tri_max]:
                    vi_tri_max = i
            gifts[vi_tri_max] = int(gifts[vi_tri_max] ** 0.5)
        tong_qua = 0
        for qua in gifts:
            tong_qua += qua
        return tong_qua
        