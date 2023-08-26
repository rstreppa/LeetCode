/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:

    // Function to transfer elements of the stack s1 to the stack s2
    void transfer(stack<ListNode*>& s1, stack<ListNode*>& s2)
    {
        while(!s1.empty()) {
            // Store the top element in a temporary variable
            ListNode* temp = s1.top();
            // Pop out of the stack
            s1.pop();
            // Push it into s2
            s2.push(temp);
        }
    }    

    ListNode* removeNodes(ListNode* head) {
        
        stack<ListNode*> mystack;

        while( head ) {
            while(!mystack.empty() && (head->val > mystack.top()->val))
                mystack.pop();
            mystack.push(head);
            head = head->next;
        }

        // reverse the stack using another stack
        stack<ListNode*> mystack_reversed; 
        transfer(mystack, mystack_reversed);

        ListNode* res  = new ListNode();
        ListNode* curr = res;
        
        // Using manual iteration since std::stack doesn't support range-based for loop
        while(!mystack_reversed.empty()) {
            ListNode* node = mystack_reversed.top();    // Get top element
            mystack_reversed.pop();                     // Remove the top element
            curr->next = node;
            curr       = curr->next;
        }
        curr->next = nullptr;                           // Important: set the 'next' of the last node to to nullptr

        return res->next;        


    }
};
