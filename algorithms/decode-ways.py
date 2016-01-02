class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        cnt,i = 0,0
        if s.startswith('0'):
            return 0
        if '00' in s:
            return 0
        while i < len(s):
            if s[i]!='0':
                cnt += 1
            if i+1 < len(s):
                #print s[i:i+2]
                if int(s[i:i+2]) < 27 and int(s[i+1]) != 0:
                    cnt +=1
            i+=2
        return cnt


s=Solution()
#print '101 - 1',s.numDecodings('101')
#print '01:',s.numDecodings('01')
print '10:',s.numDecodings('10')
#print '11:',s.numDecodings('11')
#print '27:',s.numDecodings('27')