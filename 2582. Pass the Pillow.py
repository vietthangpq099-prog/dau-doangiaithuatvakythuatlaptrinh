class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        # Thoi gian de goi di tu dau nay sang dau kia
        trip_time = n - 1
        
        # So luot di hoan chinh
        full_trips = time / trip_time
        
        # So giay di chuyen con du ra o luot hien tai
        extra_time = time % trip_time
        
        # Neu so luot hoan chinh la chan -> Goi dang di tu trai sang phai
        if full_trips % 2 == 0:
            return 1 + extra_time
        # Neu so luot hoan chinh la le -> Goi dang di tu phai ve trai
        else:
            return n - extra_time