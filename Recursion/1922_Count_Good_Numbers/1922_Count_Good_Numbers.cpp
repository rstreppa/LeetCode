class Solution {
public:
    int countGoodNumbers(long long n) {
        
        long long modulo = 1000000007;  // 10^9 + 7

        // Define binpow as std::function to allow recursion
        std::function<long long(long long, long long)> binpow =
            [&binpow, modulo](long long a, long long b) -> long long 
            {
                if (b == 0) return 1;
                auto res = binpow(a, b / 2);
                res = (res * res) % modulo;
                if (b % 2 == 1)
                    return (res * a) % modulo;
                else
                    return res;
            };
        long long l = n / 2;
        long long res;
        if (n % 2 == 1)
            res = (binpow(5, l + 1) * binpow(4, l)) % modulo;
        else
            res = (binpow(5, l) * binpow(4, l)) % modulo;

        return static_cast<int>(res % modulo);
    }
};