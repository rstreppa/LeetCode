class Solution {
    public int countCharacters(String[] words, String chars) {
        HashMap<Character, Integer> d = new HashMap<>();
        for(char c : chars.toCharArray())
            d.put(c, d.getOrDefault(c, 0) + 1);

        int res = 0;
        for(String word : words) {
            if(check(word, chars, d))
                res += word.length();
        }
        return res;             
    }

    private boolean check(String word, String chars, HashMap<Character, Integer> d) 
    {
        if(word.length() > chars.length())
            return false;
        HashMap<Character, Integer> temp = new HashMap<>();
        for(char c : word.toCharArray()) {
            temp.put(c, temp.getOrDefault(c, 0) + 1);
            if(!d.containsKey(c) || (d.get(c) < temp.get(c)))
                return false;
        }
        return true; 
    }
}