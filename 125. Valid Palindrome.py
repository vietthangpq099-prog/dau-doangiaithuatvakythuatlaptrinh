class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        trai = 0
        phai = len(s) - 1
        
        while trai < phai:
            while trai < phai and not s[trai].isalnum():
                trai += 1
            while trai < phai and not s[phai].isalnum():
                phai -= 1
            if s[trai].lower() != s[phai].lower():
            trai += 1
            phai -= 1
            
        return True