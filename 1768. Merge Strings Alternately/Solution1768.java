class Solution1768 {
    public static String mergeAlternately(String word1, String word2) {
        int min = Math.min(word1.length(), word2.length());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < min; i++) {
            sb.append(word1.charAt(i));
            sb.append(word2.charAt(i));
        }
        if (word1.length() > word2.length()) {
            sb.append(word1.substring(min));
        } else {
            sb.append(word2.substring(min));
        }
        return sb.toString();
    }
}

public static void main(String[] args) {
    System.out.println(Solution1768.mergeAlternately("abc", "pqr"));
}
