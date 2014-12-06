'''
Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter) 
'''

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        if len(s)>12:
            return []
        else:
            return self.recursiveRestore(s, 1)
        
    def recursiveRestore(self, s, depth):
        if depth == 4:
            if s.startswith('0') and len(s)!=1:
                return []
            if int(s) > 255:
                return []
            return [s]
        r = []
        for j in range(1,4):
            if len(s) - j > 3*(4-depth) or len(s)-j<4-depth:
                continue
            if int(s[0:j]) > 255:
                continue
            if s[0:j].startswith('0') and j!=1:
                continue
            subip = self.recursiveRestore(s[j:], depth+1)
            #print 'depth',depth,'j',j,'\ts',s,'\t\ts[0:j]',s[0:j],'\ts[j:]',s[j:]
            for p in subip:
                r.append(s[0:j]+'.'+p)
        #print depth,r
        return r

s=Solution()
print s.restoreIpAddresses('010010')