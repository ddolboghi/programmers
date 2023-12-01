import java.util.*;
class Solution {
    public String solution(String number, int k) {
        StringBuilder answer = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        for (char num : number.toCharArray()) {
            while (!stack.isEmpty() && (int) num - '0' > stack.peek() && k > 0) {
                stack.pop();
                k--;
            }            
            stack.push((int) num - '0');
            // System.out.println(stack);
        }
        // System.out.println(stack);
        for (Integer ele : stack) {
            answer.append(ele);
            if (answer.length() == number.length()-k) break;
        }
        return answer.toString();
    }
}