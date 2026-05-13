class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Tao mot bien tam de khong lam hong gia tri cua x ban dau
        temp = x
        digit_sum = 0
        
        # Vong lap boc tach tung chu so
        while temp > 0:
            digit_sum += temp % 10
            temp /= 10
            
        # Kiem tra tinh chat Harshad
        if x % digit_sum == 0:
            return digit_sum
            
        return -1