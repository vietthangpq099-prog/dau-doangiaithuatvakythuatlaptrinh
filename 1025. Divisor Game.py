class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Tat ca chi la mot tro choi kiem soat Chan/Le
        # Neu n chan, Alice thang (True). Neu n le, Alice thua (False).
        return n % 2 == 0