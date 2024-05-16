class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder res = new StringBuilder(); // StringBuildser because String concatenation is inefficient and will be Time Limit Exceeded
        
        int n1 = word1.length();
        int n2 = word2.length();

        if(n1==0)   
            res.append(word2);
        else if (n2==0)   
            res.append(word1);
        else {
            int i = 0;
            int j = 0;
            while(i<n1 && j<n2) {
                res.append(word1.charAt(i));
                i++;
                res.append(word2.charAt(j));
                j++;
            }
            if(i>=n1)
                res.append(word2.substring(j));
            if(j>=n2)
                res.append(word1.substring(i));
        }

        return res.toString();
    }
}