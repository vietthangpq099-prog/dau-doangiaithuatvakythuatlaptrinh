class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        idx = word.find(ch)
        # Nếu không có ký tự ch trong chuỗi, trả về nguyên bản
        if idx == -1:
            return word
        # Cắt, đảo ngược phần đầu và ghép nối với phần đuôi
        return word[:idx + 1][::-1] + word[idx + 1:]