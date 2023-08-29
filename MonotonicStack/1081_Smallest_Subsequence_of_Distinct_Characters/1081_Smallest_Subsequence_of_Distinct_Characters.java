class Solution {
    public String smallestSubsequence(String s) {
        
        HashMap<Character, Integer> hash = new HashMap<>();
        for(int i = 0; i < s.length(); i++) {
            hash.merge(s.charAt(i), 1, Integer::sum); 
        }

        List<Character> stack = new ArrayList<>();
        for(int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            hash.put(c, hash.get(c) - 1);
            if(stack.contains(c)) {
                continue;
            }
            while(!stack.isEmpty() && c < stack.get(stack.size() - 1) && hash.get(stack.get(stack.size() - 1)) > 0) {
                stack.remove(stack.size() - 1);        
            }
            stack.add(c);
        }
        
        StringBuilder res = new StringBuilder();
        for(Character c: stack) {
            res.append(c);
        }
        return res.toString();
    }
}
