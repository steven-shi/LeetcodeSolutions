'''
Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.

Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        if lenA==0 or lenB==0:
            return None
        newHeadA, newHeadB = headA, headB
        if lenA>=lenB:
            for i in range(0,lenA-lenB):
                newHeadA = newHeadA.next
        else:
            for i in range(0,lenB-lenA):
                newHeadB = newHeadB.next

        if lenA>=lenB:
            for i in range(0,lenB):
                if newHeadA.val != headB.val:
                    newHeadA = newHeadA.next
                    headB = headB.next
                else:
                    return newHeadA
        else:
            for i in range(0,lenA):
                if newHeadB.val != headA.val:
                    newHeadB = newHeadB.next
                    headA = headA.next
                else:
                    return newHeadB
        return None
    
    def getLength(self, node):
        i = 0
        while node!=None:
            i+=1
            node=node.next
        return i
'''
lnA=ListNode(1)
lnB=ListNode(2)
node=lnB
for i in range(4,12,2):
    node.next=ListNode(i)
    node=node.next
'''

s=Solution()
#print s.getLength(lnB)
print s.getIntersectionNode(lnA,lnB)