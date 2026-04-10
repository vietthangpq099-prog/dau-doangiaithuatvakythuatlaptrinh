class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            # Hoán đổi trực tiếp hai giá trị ở hai đầu
            s[left], s[right] = s[right], s[left]
            # Di chuyển hai con trỏ hướng vào giữa
            left += 1
            
            right -= 1