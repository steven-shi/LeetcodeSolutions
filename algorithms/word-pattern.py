#Given a pattern and a string str, find if str follows the same pattern.
#
#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
#Examples:
#
#    pattern = "abba", str = "dog cat cat dog" should return true.
#    pattern = "abba", str = "dog cat cat fish" should return false.
#    pattern = "aaaa", str = "dog cat cat dog" should return false.
#    pattern = "abba", str = "dog dog dog dog" should return false.
#
#Notes:
#You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space. 

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        split = str.split(' ')
        if len(pattern) != len(split):
            return False
        pattern_dic = {}
        str_dic = {}
        for i in range(0, len(split)):
            s = split[i]
            if pattern[i] not in pattern_dic and s not in str_dic:
                pattern_dic[pattern[i]] = s
                str_dic[s] = pattern[i]
            if (pattern[i] not in pattern_dic and s in str_dic) or (pattern[i] in pattern_dic and s not in str_dic):
                return False
            if pattern_dic[pattern[i]] != s:
                return False
            else:
                continue
        return True
