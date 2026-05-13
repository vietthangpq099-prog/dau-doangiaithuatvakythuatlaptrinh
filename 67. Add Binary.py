class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        
        # Lap chung nao van con bit de cong hoac van con bien nho
        while i >= 0 or j >= 0 or carry > 0:
            total = carry
            
            # Neu van con bit o chuoi a, cong vao total va lui con tro
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            # Neu van con bit o chuoi b, cong vao total va lui con tro
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # Cap nhat bien nho carry cho hang tiep theo (chia lay nguyen cho 2)
            carry = total / 2
            
            # Them bit hien tai vao ket qua (chia lay du cho 2)
            res.append(str(total % 2))
            
        # Vi phep cong thuc hien tu cuoi len dau, ta phai dao nguoc mang ket qua lai
        return "".join(res[::-1])