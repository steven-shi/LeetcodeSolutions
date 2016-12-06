#344. Reverse String
#
#Write a function that takes a string as input and returns the string reversed.
#
#Example:
#Given s = "hello", return "olleh". 

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([s[n] for n in range(len(s)-1,-1,-1)])
