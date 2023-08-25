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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode res = dummy;
        int carry       = 0;
        while(l1 != null && l2 != null)
        {
            int sum  = l1.val + l2.val + carry;
            res.next = new ListNode(sum % 10); 
            carry     = sum / 10;
            l1        = l1.next;
            l2        = l2.next;
            res       = res.next;
        }
        
        ListNode l = (l1 != null) ? l1 : l2;
        while(l != null)
        {
            int sum   = l.val + carry;
            res.next  = new ListNode(sum % 10); 
            carry     = sum / 10;
            l         = l.next;
            res       = res.next;
        }
        if( carry != 0 )
            res.next = new ListNode(carry);        

        return dummy.next;        
    }
}
