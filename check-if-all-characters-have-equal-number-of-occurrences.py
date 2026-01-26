class Solution(object):
    def areOccurrencesEqual(self, s):
        counts = {}
        for char in s:
            if char in counts:
                counts[char]+= 1
            else:
                counts[char]=1
        danh_sach_so = []
        for ky_tu in counts:
            danh_sach_so.append(counts[ky_tu]) 
        so_mau = danh_sach_so[0]
        for so in danh_sach_so:
            if so != so_mau:
                return False
        return True