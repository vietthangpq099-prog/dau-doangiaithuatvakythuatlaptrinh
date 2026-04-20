class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1 and not trust:
            return 1
            
        if len(trust) < n - 1:
            return -1
        trust_scores = [0] * (n + 1)
        for a, b in trust:
            trust_scores[a] -= 1  # a tin nguoi khac -> a mat tu cach tham phan (tru diem)
            trust_scores[b] += 1  # b duoc tin tuong -> b duoc cong diem
            
        # Kiem tra xem ai dat duoc diem so tuyet doi la n - 1
        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i
        return -1