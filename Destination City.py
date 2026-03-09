class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        for i in range(len(paths)):
            diem_den = paths[i][1]
            
            co_di_tiep_khong = False
            for j in range(len(paths)):
                if paths[j][0] == diem_den:
                    co_di_tiep_khong = True
                    break
            if co_di_tiep_khong == False:
                return diem_den
        return ""