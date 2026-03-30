class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        for i in range(n):
            tap_hang = set()
            tap_cot = set()
            # Quét qua toàn bộ phần tử trên hàng i và cột i
            for j in range(n):
                tap_hang.add(matrix[i][j])  # matrix[i][j] là duyệt theo hàng
                tap_cot.add(matrix[j][i])   # matrix[j][i] là duyệt theo cột
            # Nếu hàng hoặc cột không có đủ n phần tử khác biệt thì chốt sai
            if len(tap_hang) != n or len(tap_cot) != n:
                return False
        return True