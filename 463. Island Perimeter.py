class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        chu_vi = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # Moi o dat mac dinh dong gop 4 don vi vao chu vi
                    chu_vi += 4
                    # Neu phia Tren co dat, tuc la co 1 canh chung -> tru di 2
                    if i > 0 and grid[i-1][j] == 1:
                        chu_vi -= 2
                    # Neu phia Trai co dat, tuc la co 1 canh chung -> tru di 2
                    if j > 0 and grid[i][j-1] == 1:
                        chu_vi -= 2
        return chu_vi