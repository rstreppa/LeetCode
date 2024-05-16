class Solution {
    public String addSpaces(String s, int[] spaces) {
        StringBuilder res = new StringBuilder();    // need StringBuilder to append to string efficiently, else Time Limit Exceeded
        int j = 0;
        int n = s.length();
        for(int i=0; i<n; i++) {
            if(j<spaces.length && i==spaces[j]) {
                res.append(' ');
                j++;
            }
            res.append(s.charAt(i));
        }
        return res.toString();
    }
}