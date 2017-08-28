'''
 Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:

    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].

'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[0:k])
        if len(nums) == 1:
            return s
        tmp = s
        for i in range(1, len(nums)-k+2):
            if i+k > len(nums):
                break
            tmp = tmp-nums[i-1] + nums[i+k-1]
            if tmp > s:
                s= tmp
        return s/float(k)


            
        
x = Solution()
x.findMaxAverage([0,4,0,3,2], 1)