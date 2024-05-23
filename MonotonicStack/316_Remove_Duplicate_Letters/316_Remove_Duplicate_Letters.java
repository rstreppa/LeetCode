// Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
class Solution {
    public String removeDuplicateLetters(String s) {

        char[] ss = s.toCharArray();

        HashMap<Character, Integer> count = new HashMap<Character, Integer>();
        for (char c : ss) {
            if(count.containsKey(c)) 
                count.put(c, count.get(c) + 1);
            else 
                count.put(c, 1);            
        }

        Stack<Character> stack = new Stack<>();
        Set<Character> in_stack = new HashSet<>(); 

        for(Character c: ss) {
            
            count.put(c, count.get(c) - 1);

            if(stack.search(c) != -1)
                continue;

            while(!stack.empty() && c<stack.peek() && count.get(stack.peek())>0)
                in_stack.remove(stack.pop());
            
            stack.push(c);
            in_stack.add(c);

        }

        StringBuilder res = new StringBuilder();

	    while(!stack.empty())
		    res.append(stack.pop());

        res.reverse();

        return res.toString();
    }
}
