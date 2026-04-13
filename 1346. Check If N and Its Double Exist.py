class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        for num in arr:
            # Kiem tra xem 2 * num hoac num / 2 (neu num la so chan) co trong set chua
            if (num * 2 in seen) or (num % 2 == 0 and num // 2 in seen):
                return True 
            # Neu chua co, them num vao set de cac so phia sau kiem tra
            seen.add(num)
        return False