class Solution(object):
    def reformatNumber(self, number):
        ds_so = []
        for ky_tu in number:
            if ky_tu.isdigit():
                ds_so.append(ky_tu)
    
        ket_qua = []
        i = 0
        tong_so = len(ds_so)
        
        while (tong_so - i) > 4:
            khoi_3_so = ds_so[i] + ds_so[i+1] + ds_so[i+2]
            ket_qua.append(khoi_3_so)
            i += 3
        so_con_lai = tong_so - i
        
        if so_con_lai == 4:
            khoi_dau = ds_so[i] + ds_so[i+1]
            khoi_sau = ds_so[i+2] + ds_so[i+3]
            ket_qua.append(khoi_dau)
            ket_qua.append(khoi_sau)
            
        else:
            khoi_cuoi = ""
            for k in range(i, tong_so):
                khoi_cuoi += ds_so[k]
            ket_qua.append(khoi_cuoi)
            
        return "-".join(ket_qua)
        