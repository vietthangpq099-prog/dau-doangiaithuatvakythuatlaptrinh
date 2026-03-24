class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        chan = []
        le = []
        for i in range(len(nums)):
            if i % 2 == 0:
                chan.append(nums[i])
            else:
                le.append(nums[i])
                chan.sort() 
        le.sort(reverse=True)  
        
        ket_qua = []
        i_chan = 0
        i_le = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ket_qua.append(chan[i_chan])
                i_chan += 1
            else:
                ket_qua.append(le[i_le])
                i_le += 1
        return ket_qua
