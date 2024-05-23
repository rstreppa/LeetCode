class Solution {
public:
    int minSetSize(vector<int>& arr) {
        int n = arr.size();
        unordered_map<int, int> d;
        for(auto& num: arr)
            d[num]++;
        
        vector<int> values;
        for (auto& it: d)
            values.push_back(it.second);
        sort(values.begin(), values.end(), greater<>());
        
        int summation = 0;
        int res = 0;
        for(auto& v: values) {
            summation += v;
            res++;
            if(summation >= n/2)
                break;

        }
        return res;
    }
};