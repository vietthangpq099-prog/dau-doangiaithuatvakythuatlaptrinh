class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        tong_thoi_gian = 0
        ve_cua_k = tickets[k]
        for vi_tri in range(len(tickets)):
            if vi_tri <= k:
                if tickets[vi_tri] < ve_cua_k:
                    tong_thoi_gian += tickets[vi_tri]
                else:
                    tong_thoi_gian += ve_cua_k
            else:
                if tickets[vi_tri] < ve_cua_k - 1:
                    tong_thoi_gian += tickets[vi_tri]
                else:
                    tong_thoi_gian += ve_cua_k - 1
        return tong_thoi_gian