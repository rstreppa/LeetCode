class Solution {
    public int binaryGap(int n) {
        String binary = Integer.toBinaryString(n);
        
        if (binary.length() < 2) {
            return 0;
        }

        int max_gap = 0;
        Integer last_one_pos = null;

        for (int i = 0; i < binary.length(); i++) {
            char e = binary.charAt(i);
            if (e == '1') {
                if (last_one_pos != null) {
                    max_gap = Math.max(max_gap, i - last_one_pos);
                }
                last_one_pos = i;
            }
        }

        return max_gap;        
    }
}
