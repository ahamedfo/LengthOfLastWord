class Solution(object):
    def lengthOfLastWord(self, s):
        i = 0
        word_found = False
        for k in range(len(s) - 1, -1, -1):
            if s[k] == ' ' and word_found == True:
                return i
            elif s[k] != ' ':
                i += 1
                word_found = True
        return i

    