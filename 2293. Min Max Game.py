class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Tiep tuc to chuc giai dau neu van con nhieu hon 1 nguoi
        while len(nums) > 1:
            n = len(nums)
            # Tao mang luu ket qua cua vong hien tai (kich thuoc giam 1 nua)
            newNums = [0] * (n / 2)
            
            # Xet tung cap dau
            for i in range(n / 2):
                # Neu la tran dau mang so thu tu chan -> Chon Min
                if i % 2 == 0:
                    newNums[i] = min(nums[2 * i], nums[2 * i + 1])
                # Neu la tran dau mang so thu tu le -> Chon Max
                else:
                    newNums[i] = max(nums[2 * i], nums[2 * i + 1])
                    
            # Chuyen sang vong dau tiep theo bang cach cap nhat mang nums
            nums = newNums
            
        # Nguoi song sot cuoi cung la nha vo dich
        return nums[0]