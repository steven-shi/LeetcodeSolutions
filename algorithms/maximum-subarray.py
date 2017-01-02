'''
53. Maximum Subarray
 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

 For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
 the contiguous subarray [4,-1,2,1] has the largest sum = 6. 
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = [0]*len(nums)
        maximum[0] = nums[0]
        ma = nums[0]
        for n in range(1,len(nums)):
            if maximum[n-1] > 0:
                maximum[n]=maximum[n-1]+nums[n]
            else:
                maximum[n]=nums[n]
        return max(maximum)
