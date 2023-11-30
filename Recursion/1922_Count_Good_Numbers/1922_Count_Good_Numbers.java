class Solution {
    private static final long MODULO = 1000000007L;  // 10^9 + 7

    public int countGoodNumbers(long n) {
        long l = n / 2;
        long res;
        if (n % 2 == 1)
            res = (binpow(5, l + 1) * binpow(4, l)) % MODULO;
        else
            res = (binpow(5, l) * binpow(4, l)) % MODULO;

        return (int)(res % MODULO);
    }

    private long binpow(long base, long exponent) {
        long result = 1;
        while (exponent > 0) {
            if (exponent % 2 == 1)
                result = (result * base) % MODULO;
            base = (base * base) % MODULO;
            exponent /= 2;
        }
        return result;
    }
}