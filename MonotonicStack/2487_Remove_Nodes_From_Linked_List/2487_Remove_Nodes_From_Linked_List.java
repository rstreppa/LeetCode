/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNodes(ListNode head) {
        // Initialize an empty stack to hold nodes in decreasing order of their values.
        ArrayList<ListNode> stack = new ArrayList<>();

        // Iterate through the list and populate the stack.
        while (head != null) {
            while (!stack.isEmpty() && head.val > stack.get(stack.size() - 1).val) {
                stack.remove(stack.size() - 1);
            }
            stack.add(head);
            head = head.next;
        }

        // Create a dummy node to serve as the new head of the list.
        ListNode res = new ListNode();
        ListNode curr = res;

        // Update 'next' pointers to build the final list.
        for (ListNode node : stack) {
            curr.next = node;
            curr = curr.next;
        }
        curr.next = null;  // Important: set the 'next' of the last node to null.

        return res.next;      
    }
}
