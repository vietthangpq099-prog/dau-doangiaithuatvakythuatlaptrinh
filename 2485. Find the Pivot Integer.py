class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Tinh tong tat ca cac so tu 1 den n
        tong_s = n * (n + 1) // 2
        # Tinh can bac 2 cua tong (ep kieu ve so nguyen)
        x = int(tong_s ** 0.5)
        # Kiem tra xem x co dung la can bac 2 hoan hao khong
        if x * x == tong_s:
            return x
        # Neu khong phai so chinh phuong, khong ton tai x
        return -1