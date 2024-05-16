class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string res = "";
        size_t n = s.length();
        size_t j = 0;
        for(size_t i=0; i<n; i++) {
            if(j<spaces.size() && i==spaces[j]) {
                res.push_back(' ');
                j++;
            }
            res.push_back(s[i]);
        }

        return res;
    }
};