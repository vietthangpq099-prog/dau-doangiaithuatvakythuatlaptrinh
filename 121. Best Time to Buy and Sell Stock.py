class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            # Neu thay gia thap hon, cap nhat lai mien mua vao
            if price < min_price:
                min_price = price
            # Neu gia cao hon, thu tinh loi nhuan va so sanh voi muc ky luc
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit