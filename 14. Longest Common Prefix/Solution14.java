class Solution14 {
    public static String longestCommonPrefix(String[] strs) {
        int min = Integer.MAX_VALUE;
        for (String string : strs) {
            if (string.length() < min) {
                min = string.length();
            }
        }
        int i = 0;
        while (i < min) {
            for (String str : strs) {
                if (str.charAt(i) != strs[0].charAt(i)) {
                    return str.substring(0, i);
                }
            }
            i++;
        }
        return strs[0].substring(0, i);
    }

    public static void main(String[] args) {
        String[] arr = { "ab", "a" };
        System.out.println(longestCommonPrefix(arr));

    }
}