class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        min1 = float('inf')
        min2 = float('inf')
        
        # Duyet qua tung muc gia trong cua hang
        for p in prices:
            # Neu tim thay mon re hon ca min1
            if p < min1:
                # min1 cu se bi day xuong thanh mon re thu 2
                min2 = min1
                # Cap nhat lai mon re nhat
                min1 = p
            # Neu mon nay khong re hon min1, nhung lai re hon min2 hien tai
            elif p < min2:
                # Cap nhat lai mon re thu 2
                min2 = p
                
        # Tinh tong tien 2 mon re nhat
        cost = min1 + min2
        
        # Kiem tra xem co du tien mua khong (khong bi am)
        if cost <= money:
            return money - cost
            
        # Neu van khong du tien, khong mua gi ca va mang tien ve
        return money