class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        unordered_map<char, int> d;
        for(char c : chars)
            d[c]++;
        int res = 0;
        for(string word : words) {
            if(check(word, chars, d))
                res += word.length();
        }
        return res;                
    }
private:
    bool check(string word, string chars, unordered_map<char, int> d) 
    {
        if(word.length() > chars.length())
            return false;
        unordered_map<char, int> temp;
        for(char c : word) {
            temp[c]++;
            if((d.find(c) == d.end()) || (d[c] < temp[c]))
                return false;
        }
        return true; 
    }
};