class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: boolz
        """
        # Tach toa do x, y cua tung diem de de quan ly
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        # Kiem tra bang phep nhan cheo xem 3 diem co KHONG thang hang hay khong
        # Neu 2 ve khac nhau -> Khong thang hang -> La Boomerang (True)
        # Neu 2 ve bang nhau -> Thang hang hoac bi trung diem -> False
        return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)