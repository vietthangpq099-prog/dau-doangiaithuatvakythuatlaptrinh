class Solution(object):
    def distributeCandies(self, candies, num_people):
        ket_qua = [0] * num_people
        so_keo_can_dua = 1

        nguoi_hien_tai = 0
        while candies > 0:
            if candies >= so_keo_can_dua:
                ket_qua[nguoi_hien_tai] += so_keo_can_dua
    
                candies -= so_keo_can_dua
                so_keo_can_dua += 1
            else:
                ket_qua[nguoi_hien_tai] += candies
                candies = 0
            nguoi_hien_tai += 1
            if nguoi_hien_tai == num_people:
                nguoi_hien_tai = 0
        return ket_qua
        