''' 414. Third Maximum Number
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:

Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.

Example 2:

Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = []
        for i in nums:
            if len(r) == 0:
                r.append(i)
                continue
            for l in range(len(r)):
                if i>r[l]:
                    r.insert(l, i)
                    break
                if i==r[l]:
                    break
                if l == len(r)-1:
                    r.append(i)
            r = r[:min(len(r),3)]
        
        return r[-1] if len(r)==3 else r[0]
