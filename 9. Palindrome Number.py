class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Bat ky so am nao, hoac so ket thuc bang 0 (nhung khong phai so 0) deu bi loai
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reverted_half = 0
        
        # Dao nguoc nua sau cua con so de so sanh voi nua dau
        while x > reverted_half:
            # Tach chu so hang don vi cua x va day vao reverted_half
            reverted_half = reverted_half * 10 + x % 10
            # Vut bo chu so hang don vi cua x
            x /= 10
        # Kiem tra doi xung cho ca truong hop chieu dai chan va chieu dai le
        return x == reverted_half or x == reverted_half / 10