danh_sach_ket_hop = []
        
        # Lấy số lượng người (n)
        so_nguoi = len(names)
        
        # 1. Ghép chiều cao và tên của từng người lại
        for i in range(so_nguoi):
            # Lưu chiều cao trước, tên sau
            # Vì khi sort, Python sẽ so sánh phần tử đầu tiên (chiều cao) trước
            cap_du_lieu = [heights[i], names[i]]
            danh_sach_ket_hop.append(cap_du_lieu)
            
        # 2. Sắp xếp danh sách đó giảm dần (người cao đứng đầu)
        # reverse=True nghĩa là sắp xếp ngược (lớn đến bé)
        danh_sach_ket_hop.sort(reverse=True)
        
        # 3. Tách lấy phần tên ra để trả về kết quả
        ket_qua = []
        for cap in danh_sach_ket_hop:
            # cap[0] là chiều cao, cap[1] là tên
            ten = cap[1]
            ket_qua.append(ten)
            
        return ket_qua