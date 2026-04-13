class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            # Nếu stack không rỗng và phần tử trên cùng giống phần tử hiện tại
            if stack and stack[-1] == char:
                stack.pop()  # Loại bỏ phần tử trên cùng (xóa cặp trùng lặp)
            else:
                stack.append(char)  # Nếu không trùng, thêm vào stack
        return "".join(stack)
        