class Solution392 {
    public static boolean isSubsequence(String s, String t) {

        for (int i = 0; i < t.length(); i++) {
            if (s.length() == 0)
                break;
            if (s.charAt(0) == t.charAt(i)) {
                s = s.substring(1);
            }
        }
        return s.length() == 0;
    }
}

public static void main(String[] args) {
    System.out.println(Solution392.isSubsequence("b", "abc"));
}