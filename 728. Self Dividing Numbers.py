class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        
        # Duyet qua tung con so trong khoang tu left den right
        for num in range(left, right + 1):
            temp = num
            is_valid = True
            
            # Tach tung chu so cua temp de kiem tra
            while temp > 0:
                digit = temp % 10
                
     # Loai bo ngay lap tuc neu chu so la 0 HOAC num khong chia het cho chu so do
                if digit == 0 or num % digit != 0:
                    is_valid = False
                    break
                # Vut bo chu so hang don vi de tiep tuc xet chu so tiep theo
                temp /= 10 
            # Neu qua duoc het cac bai kiem tra, day la so tu chia hop le
            if is_valid:
                result.append(num)    
        return result