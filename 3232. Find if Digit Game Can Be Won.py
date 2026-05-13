class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        single_sum = 0
        double_sum = 0
        
        # Duyet qua tung con so tren ban choi
        for num in nums:
            if num < 10:
                # Nhom 1 chu so
                single_sum += num
            else:
                # Nhom 2 chu so
                double_sum += num
                
        # Alice se thang mien la 2 tong nay khac nhau (khong bi hoa)
        return single_sum != double_sum