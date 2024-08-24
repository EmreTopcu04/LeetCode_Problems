
import java.util.HashMap;

class Solution13 {
    public static int romanToInt(String s) {
        HashMap<Character, Integer> romanMap = new HashMap<Character, Integer>();
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);
        romanMap.put('L', 50);
        romanMap.put('C', 100);
        romanMap.put('D', 500);
        romanMap.put('M', 1000);
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i < s.length() - 1 && romanMap.get(s.charAt(i)) < romanMap.get(s.charAt(i + 1))) {
                sum += romanMap.get(s.charAt(i + 1)) - romanMap.get(s.charAt(i));
                i++;
            } else {
                sum += romanMap.get(s.charAt(i));
            }

        }
        return sum;
    }
}

public static void main(String[] args) {
    System.out.println(Solution13.romanToInt("MCMXCIV"));
}
