class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        cac_hop = {}
        for so_bong in range(lowLimit, highLimit + 1):
            
            chuoi_so = str(so_bong)
            tong_chu_so = 0
            for ky_tu in chuoi_so:
                tong_chu_so += int(ky_tu)
            if tong_chu_so in cac_hop:
                cac_hop[tong_chu_so] += 1
            else:
                cac_hop[tong_chu_so] = 1
        
        so_bong_nhieu_nhat = 0
        
        danh_sach_so_luong = list(cac_hop.values())
        
        for so_luong in danh_sach_so_luong:
            if so_luong > so_bong_nhieu_nhat:
                so_bong_nhieu_nhat = so_luong
                
        return so_bong_nhieu_nhat
        