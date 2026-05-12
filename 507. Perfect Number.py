class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
            
        # Luon bat dau tong bang 1 vi 1 la uoc cua moi so duong
        tong_uoc_so = 1
        
        # Chi can duyet tu 2 den can bac hai cua num
        i = 2
        while i * i <= num:
            # Neu tim thay mot uoc so
            if num % i == 0:
                tong_uoc_so += i
                
                # Cong them uoc so doi xung cua no (neu khac voi i de tranh cong trung)
                if i * i != num:
                    tong_uoc_so += num / i         
            i += 1  
        # Kiem tra xem tong cac uoc co bang chinh con so do hay khong
        return tong_uoc_so == num