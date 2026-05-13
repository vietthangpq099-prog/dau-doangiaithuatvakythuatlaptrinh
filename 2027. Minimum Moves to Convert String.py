class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        moves = 0
        i = 0
        
        # Duyet qua tung ky tu trong chuoi
        while i < len(s):
            # Neu phat hien ky tu X, bat buoc phai tieu ton 1 buoc bien doi
            if s[i] == 'X':
                moves += 1
                # Nhay coc 3 buoc vi ky tu hien tai va 2 ky tu sau do da tro thanh O
                i += 3
            else:
                # Neu la O, chi can bo qua va xet ky tu tiep theo
                i += 1
                
        return moves