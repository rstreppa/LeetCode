class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        if (n == 0) {
            return 0;
        }
        
        int res = 1;
        HashMap<Character, Integer> d = new HashMap<>();
        int i = 0, j = 0;
        
        while (j < n) 
        {
            if ( d.get(s.charAt(j)) == null || d.get(s.charAt(j)) == 0) {
                d.put(s.charAt(j), 1);
                res = Math.max(res, j - i + 1);
                j++;
            } else {
                d.put(s.charAt(i), d.get(s.charAt(i)) - 1);
                i++;
            }
        }
        return res;            
    }
}
