import java.util.*;
import java.lang.Math.*;

class Solution {
    String leftFinger = "*";
    String rightFinger = "#";
    
    public String solution(int[] numbers, String hand) {
        String answer = "";
        
        List<String> leftLow = List.of("1","4","7");
        List<String> rightLow = List.of("3","6","9");
        
        for (int i=0;i<numbers.length;i++) {
            String number = Integer.toString(numbers[i]);
            if (leftLow.contains(number)) {
                leftFinger = number;
                answer += "L";
            } else if (rightLow.contains(number)) {
                rightFinger = number;
                answer += "R";
            } else {
                answer += getMidFinger(number, hand);
            }
        }
        return answer;
    }
    
    private String getMidFinger( 
        String number,
        String hand
    ) {
        String[][] keypad = {{"1","2","3"},
                             {"4","5","6"},
                             {"7","8","9"},
                             {"*","0","#"}};
        
        int[] numberPos = new int[2];
        int[] leftPos = new int[2];
        int[] rightPos = new int[2];
        
        for (int row=0;row<keypad.length;row++){
            for (int col=0;col<keypad[row].length;col++){
                String word = keypad[row][col];
                if (word.equals(number)) {
                    numberPos[0] = row;
                    numberPos[1] = col;
                }
                if (word.equals(leftFinger)) {
                    leftPos[0] = row;
                    leftPos[1] = col;
                }
                if (word.equals(rightFinger)) {
                    rightPos[0] = row;
                    rightPos[1] = col;
                }
            }
        }
        
        int leftDistance = Math.abs(numberPos[0]-leftPos[0])
            + Math.abs(numberPos[1]-leftPos[1]);
        
        int rightDistance = Math.abs(numberPos[0]-rightPos[0]) 
            + Math.abs(numberPos[1]-rightPos[1]);
        
        if (leftDistance == rightDistance) {
            if (hand.equals("right")) {
                rightFinger = number;
                return "R";
            } else {
                leftFinger = number;
                return "L";
            }
        } else if (leftDistance > rightDistance) {
            rightFinger = number;
            return "R";
        } else {
            leftFinger = number;
            return "L";
        }
        
    }
}
                
                