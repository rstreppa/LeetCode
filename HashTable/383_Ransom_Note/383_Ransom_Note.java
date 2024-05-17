class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> r = new HashMap<>();
        HashMap<Character, Integer> m = new HashMap<>();

        for(Character c : ransomNote.toCharArray())
            r.merge(c, 1, Integer::sum); 

        for(Character c : magazine.toCharArray())
            m.merge(c, 1, Integer::sum); 

        for(Map.Entry<Character, Integer> e : r.entrySet()) {
            char key = e.getKey();    
            Integer value = e.getValue(); 
            if(!m.containsKey(key))
                return false;
            if(m.get(key)<value)
                return false;

        }
        return true;        
    }
}