# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        2487. Remove Nodes From Linked List
        Medium
 
        You are given the head of a linked list.
        Remove every node which has a node with a strictly greater value anywhere to the right side of it.
        Return the head of the modified linked list.

        Example 1:
        Input: head = [5,2,13,3,8]
        Output: [13,8]
        Explanation: The nodes that should be removed are 5, 2 and 3.
        - Node 13 is to the right of node 5.
        - Node 13 is to the right of node 2.
        - Node 8 is to the right of node 3.
        
        Example 2:
        Input: head = [1,1,1,1]
        Output: [1,1,1,1]
        Explanation: Every node has value 1, so no nodes are removed.
        """

        # 1 Initialize an Empty Monotonic Stack: The stack will hold nodes from the linked list and will be maintained in decreasing order 
        # of their values.

        # 2 Iterate Through the List: For each node, 
        #   *   While the stack is not empty and the current node's value is greater than the value 
        #       of the node at the top of the stack, pop nodes from the stack.
        #   *   Push the current node onto the stack.

        # 3 Update next Pointers: Once the stack is fully populated, you can simply update the next pointers of the nodes in the stack 
        # to build the final list.

        # By directly manipulating the next pointers, you can solve this problem in one pass through the linked list, improving efficiency.
        # used a for loop to iterate through the stack. This keeps the overall time complexity at O(n).
        
        stack = []

        while head:
            while stack and head.val > stack[-1].val:
                stack.pop()
            stack.append(head)
            head = head.next

        res = ListNode()
        curr = res
        for node in stack:
            curr.next = node
            curr = curr.next
        curr.next = None  # Important: set the 'next' of the last node to None

        return res.next
