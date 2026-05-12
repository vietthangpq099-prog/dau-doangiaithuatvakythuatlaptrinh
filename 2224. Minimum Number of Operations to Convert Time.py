class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        # Cat chuoi [0:2] de lay gio, [3:5] de lay phut
        current_mins = int(current[0:2]) * 60 + int(current[3:5])
        correct_mins = int(correct[0:2]) * 60 + int(correct[3:5])
        
        # 2. Tinh khoang thoi gian chenh lech can bu dap
        diff = correct_mins - current_mins
        
        operations = 0
        
        # 3. Ap dung thuat toan Tham lam voi cac "menh gia" buoc nhay
        for step in [60, 15, 5, 1]:
            # Cong so buoc nhay toi da the thuc hien voi menh gia nay
            operations += diff / step
            
            # Cap nhat lai khoang thoi gian con thieu
            diff %= step
            
        return operations