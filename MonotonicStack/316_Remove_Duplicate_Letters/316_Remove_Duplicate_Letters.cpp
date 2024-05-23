// Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
class Solution {
public:
    string removeDuplicateLetters(string s) {
        
        unordered_map<char, unsigned int> count;
        for(auto& c: s)
            count[c]++;
    
        stack<char> stack;
        set<char> in_stack;

        for(auto& c: s) {
            
            count[c]--;
            
            if(is_in_stack(c, stack))
                continue;

            while(!stack.empty() && c<stack.top() && count[stack.top()]>0) {
                in_stack.erase(stack.top());
                stack.pop();
            }

            stack.push(c);
            in_stack.insert(c);

        }

    	string res;
	    while(!stack.empty()) {
		    res.push_back(stack.top());
		    stack.pop();
	    }
        reverse(res.begin(), res.end());

        return res;
    
    }

    bool is_in_stack(char c, stack<char> stack) {
        while (!stack.empty()) {
            if (stack.top() == c) return true;
            stack.pop();
        }
        return false;
    }


};