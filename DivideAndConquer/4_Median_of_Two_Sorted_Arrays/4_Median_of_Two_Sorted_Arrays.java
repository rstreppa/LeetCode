class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A, B;
        if (nums1.length <= nums2.length) {
            A = nums1;
            B = nums2;
        } else {
            A = nums2;
            B = nums1;
        }

        int m = A.length;
        int n = B.length;
        int half_len = (m + n + 1) / 2;
        int leftA = 0, rightA = m;

        while (leftA <= rightA) {
            int i = (leftA + rightA) / 2;
            int j = half_len - i;

            if (i < m && B[j-1] > A[i]) {
                leftA = i + 1;
            } else if (i > 0 && A[i-1] > B[j]) {
                rightA = i - 1;
            } else {
                int max_of_left;
                if (i == 0) max_of_left = B[j-1];
                else if (j == 0) max_of_left = A[i-1];
                else max_of_left = Math.max(A[i-1], B[j-1]);

                if ((m + n) % 2 == 1) {
                    return (double) max_of_left;
                }

                int min_of_right;
                if (i == m) min_of_right = B[j];
                else if (j == n) min_of_right = A[i];
                else min_of_right = Math.min(A[i], B[j]);

                return (max_of_left + min_of_right) / 2.0;
            }
        }

        return 0.0;  // This should never happen        
    }
}
