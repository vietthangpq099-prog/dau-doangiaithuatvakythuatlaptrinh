class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        tong_da_uong = numBottles
        vo_chai = numBottles 
        while vo_chai >= numExchange:
            chai_moi = vo_chai // numExchange 
            vo_le = vo_chai % numExchange     
            tong_da_uong = tong_da_uong + chai_moi 
            vo_chai = chai_moi + vo_le 
        return tong_da_uong