class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def heapify(n, i):
            while True:
                lon_nhat = i
                trai = 2 * i + 1
                phai = 2 * i + 2
                
         
                if trai < n and nums[trai] > nums[lon_nhat]:
                    lon_nhat = trai
                if phai < n and nums[phai] > nums[lon_nhat]:
                    lon_nhat = phai
                if lon_nhat != i:
                    nums[i], nums[lon_nhat] = nums[lon_nhat], nums[i]
                    i = lon_nhat  
                else:
                    break  
                    
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
        for i in range(n - 1, 0, -1):
         
            nums[i], nums[0] = nums[0], nums[i]
            heapify(i, 0)
        return nums