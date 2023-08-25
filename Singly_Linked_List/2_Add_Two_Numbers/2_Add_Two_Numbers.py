# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        2. Add Two Numbers
        Medium
        
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        
        Example 1:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
        
        Example 2:
        Input: l1 = [0], l2 = [0]
        Output: [0]
        
        Example 3:
        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]
        
        """
        dummy = ListNode(0)  # Create a dummy node
        res = dummy  # Point 'res' to dummy node
        carry = 0
        while l1 and l2:
            mysum = l1.val + l2.val + carry
            res.next = ListNode(mysum % 10) 
            carry = mysum // 10
            l1  = l1.next
            l2  = l2.next
            res = res.next
            
        l = l1 or l2
        while l:
            mysum = l.val + carry
            res.next = ListNode(mysum % 10) 
            carry = mysum // 10
            l   = l.next
            res = res.next
        
        if carry != 0:
            res.next = ListNode(carry)        

        return dummy.next
