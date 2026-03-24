class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        tong_tien = 0
        for i in range(len(cost)):
            if (i + 1) % 3 == 0:
                continue
            tong_tien += cost[i]
        return tong_tien