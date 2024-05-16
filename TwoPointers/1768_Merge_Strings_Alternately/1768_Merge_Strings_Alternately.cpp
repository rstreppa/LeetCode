class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string res = "";
        size_t n1 = word1.length();
        size_t n2 = word2.length();

        size_t i = 0, j = 0;
        while(i<n1 && j<n2) {
            res += word1[i++];
            res += word2[j++];
        }
        while(i<n1) {
            res += word1[i++];
        }
        while(j<n2) {
            res += word1[j++];
        }
        
        return res;
    }       
};