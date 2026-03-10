class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        clean_paragraph = ""
        for char in paragraph:
            if char in "!?',;.":
                clean_paragraph += " "  # Gặp dấu câu thì thay bằng dấu cách
            else:
                clean_paragraph += char
        clean_paragraph = clean_paragraph.lower()
        word_list = clean_paragraph.split()
        word_count = {}
        for word in word_list:
            if word not in banned:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        most_common_word = ""
        max_count = 0
        for word in word_count:
            if word_count[word] > max_count:
                max_count = word_count[word]
                most_common_word = word
        return most_common_word