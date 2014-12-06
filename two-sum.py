'''
Two Sum

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 '''

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dic ={}
        for i in range(len(num)):
            if num[i] in dic:
                dic[num[i]].append(i+1)
                continue
            dic[num[i]] = [i+1]
        for i in num:
            if target-i in dic:
                if target == 2*i:
                    if len(dic[i])==1:
                        continue
                    else:
                        return (dic[i][0], dic[i][1])
                else:
                    index1 = dic[target-i][0]
                    index2 = dic[i][0]
                    return (min(index1, index2),max(index1,index2))
        return ()