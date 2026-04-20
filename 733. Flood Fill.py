class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        ma_mau_cu = image[sr][sc]
        if ma_mau_cu == color:
            return image
            
        rows = len(image)
        cols = len(image[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != ma_mau_cu:
                return
                
            # To mau moi cho o hien tai
            image[r][c] = color
            
            # De quy loang tiep ra 4 huong xung quanh
            dfs(r - 1, c) # Len tren
            dfs(r + 1, c) # Xuong duoi
            dfs(r, c - 1) # Sang trai
            dfs(r, c + 1) # Sang phai
            
        dfs(sr, sc)
        return image
