'''387. First Unique Character in a String
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

 Examples:

 s = "leetcode"
 return 0.

 s = "loveleetcode",
 return 2.

 Note: You may assume the string contain only lowercase letters. 
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = {}
        for idx, val in enumerate(s):
            if val in c:
                c[val] = -1
            else:
                c[val] = idx
        r = -1
        for v in c.values():
            if v>=0:
                if r == -1:
                    r=v
                elif r>v:
                    r=v
        return r
