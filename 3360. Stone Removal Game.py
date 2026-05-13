class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # So da can lay o luot dau tien la 10
        stones_to_remove = 10
        
        # Bien boolean kiem soat luot choi (True nghia la den luot Alice)
        alice_turn = True
        
        # Tro choi tiep tuc neu so da con lai tren ban du de nhat
        while n >= stones_to_remove:
            n -= stones_to_remove      # Nhat da
            stones_to_remove -= 1      # Giam so da yeu cau cho luot tiep theo
            alice_turn = not alice_turn # Dao luot choi
            
 # Neu vong lap dung, nguoi dang cam luot (alice_turn) se khong the nhat du da va bi thua.
        # Tuc la neu alice_turn dang la True -> Alice thua -> Tra ve False
        # Neu alice_turn dang la False -> Bob thua -> Alice thang -> Tra ve True
        return not alice_turn