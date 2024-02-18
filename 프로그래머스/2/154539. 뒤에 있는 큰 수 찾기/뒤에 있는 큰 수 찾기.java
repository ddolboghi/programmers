import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        answer[numbers.length-1] = -1;
        Stack<Integer> preMaxs = new Stack<>();
        preMaxs.push(-1);
        for (int i = numbers.length-2; i > -1; i--) {
            if (numbers[i] < numbers[i+1]) {
                preMaxs.push(numbers[i+1]);
                answer[i] = numbers[i+1];
            } else {
                while (preMaxs.peek() <= numbers[i] && preMaxs.peek() != -1) {
                    preMaxs.pop();
                }
                answer[i] = preMaxs.peek();
            }
            // System.out.println(i+" "+preMaxs);
        }
        
        return answer;
    }
}