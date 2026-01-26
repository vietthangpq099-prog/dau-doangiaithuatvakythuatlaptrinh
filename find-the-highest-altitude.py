class Solution(object):
    def largestAltitude(self, gain):
        danh_sach_do_cao = [0]
        
        do_cao_hien_tai = 0
        
        for chenh_lech in gain:
            do_cao_hien_tai += chenh_lech
            danh_sach_do_cao.append(do_cao_hien_tai)
        max_height = danh_sach_do_cao[0]
        for h in danh_sach_do_cao:
            if h > max_height:
                max_height = h
        return max_height