class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
            
        # Cong thuc toan hoc O(1) de tinh Digital Root
        return 1 + (num - 1) % 9