class Solution {
    public int solution(String str1, String str2) {
        for (int i = 0; i < str1.length(); i++) {
            int end = str2.length() + i;
            if (end > str1.length()) {
                return 2;
            } else if (str1.substring(i, end).equals(str2)) {
                return 1;
            }
        }
        return 2;
    }
}