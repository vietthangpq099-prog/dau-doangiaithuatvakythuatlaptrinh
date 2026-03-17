class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        check_index = 0
        if ruleKey == "type":
            check_index = 0
        elif ruleKey == "color":
            check_index = 1
        elif ruleKey == "name":
            check_index = 2
        match_count = 0
        for item in items:
            if item[check_index] == ruleValue:
                match_count += 1  # Đếm thêm 1 món  
        return match_count