class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        best = ""
        for i in range(len(s) - 1, 0, -1):
            for j in range(i + 1):
                if s[i] == s[j]:
                    idx = j - 1
                    if j == 0:
                        idx = None
                    str1 = s[j:i+1]
                    str2 = s[i:idx:-1]
                    if str1 == str2:
                        if len(str1) > len(best):
                            best = str1
        return best