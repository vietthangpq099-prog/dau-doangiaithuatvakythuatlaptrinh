class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            new_s = ""
            
            # Buoc nhay k de cat chuoi thanh cac nhom
            for i in range(0, len(s), k):
                # Lay nhom chu so hien tai
                group = s[i : i+k]
                
                # Tinh tong cac chu so trong nhom nay
                tong = 0
                for char in group:
                    tong += int(char)
                    
                # Chuyen tong thanh chuoi va ghep vao new_s
                new_s += str(tong)
                
            # Cap nhat s bang chuoi moi sau khi hoan thanh 1 vong
            s = new_s
            
        return s