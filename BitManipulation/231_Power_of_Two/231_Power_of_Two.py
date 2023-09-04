    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool

        231. Power of Two
        Easy
        Given an integer n, return true if it is a power of two. Otherwise, return false.
        An integer n is a power of two, if there exists an integer x such that n == 2^x.
        """
        # if n is a power of two n & (n-1) is 0 as the & will be always between a 0 and a 1
        # special case if n=0 itself, not a power of two
        
        return n and not(n & (n-1))
