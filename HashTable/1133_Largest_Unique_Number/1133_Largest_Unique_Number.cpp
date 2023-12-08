#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int largestUniqueNumber(vector<int>& A) {
        unordered_map<int, int> countMap;
        for (int num : A) {
            countMap[num]++;
        }

        vector<int> uniqueNums;
        for (auto& it : countMap) {
            if (it.second == 1) {
                uniqueNums.push_back(it.first);
            }
        }

        if (uniqueNums.empty()) {
            return -1;
        }

        sort(uniqueNums.begin(), uniqueNums.end());
        return uniqueNums.back();
    }
};
