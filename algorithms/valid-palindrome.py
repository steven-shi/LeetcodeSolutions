'''
Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome. 
'''

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i,j = 0, len(s)-1
        while i<=j:
            while i<=j:
                if not s[i].isalnum():
                    i+=1
                else:
                    break
            while i<=j:
                if not s[j].isalnum():
                    j-=1
                else:
                    break
            if j<i:
                break
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
        
s=Solution()
print s.isPalindrome(' ')