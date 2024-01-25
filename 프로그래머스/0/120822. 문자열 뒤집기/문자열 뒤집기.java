class Solution {
    public String solution(String my_string) {
        String answer = "";
        char[] str = my_string.toCharArray();
        for (int i = str.length-1; i > -1; i--) {
            answer += str[i];
        }
        return answer;
    }
}