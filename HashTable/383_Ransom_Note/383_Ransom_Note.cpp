class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> r;
        unordered_map<char, int> m;

        for(auto& c: ransomNote)
            ++r[c];

        for(auto& c: magazine)
            ++m[c];

        for (auto& it: r) {
            if (m.find(it.first) == m.end())
                return false;
            if(m[it.first] < it.second)
                return false;
        }
        return true;
    }
};