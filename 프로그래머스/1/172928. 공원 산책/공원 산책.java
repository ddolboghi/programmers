import java.util.*;
class Solution {
    public int[] solution(String[] park, String[] routes) {
        int x = 0;
        int y = 0;
        for (int i = 0; i < park.length; i++) {
            for (int j = 0; j < park[i].length(); j++) {
                if (park[i].charAt(j) == 'S') {
                    x = j;
                    y = i;
                }
            }
        }
        int outX = park[0].length();
        int outY = park.length;
        
        for (String r : routes) {
            int move = r.charAt(2) - '0';
            char dir = r.charAt(0);
            int initX = x;
            int initY = y;
            if (dir == 'E' && initX + move < outX) {
                for (int i = initX; i <= initX + move; i++) {
                    if (park[initY].charAt(i) == 'X') {
                        x = initX;
                        break;
                    }
                    x = initX + move;
                }
            } else if (dir == 'W' && initX - move >= 0) {
                for (int i = initX; i >= initX - move; i--) {
                    if (park[initY].charAt(i) == 'X') {
                        x = initX;
                        break;
                    }
                    x = initX - move;
                }
            } else if (dir == 'N' && initY - move >= 0) {
                for (int i = initY; i >= initY - move; i--) {
                    if (park[i].charAt(initX) == 'X') {
                        y = initY;
                        break;
                    }
                    y = initY - move;
                }
            } else if (dir == 'S' && initY + move < outY) {
                for (int i = initY; i <= initY + move; i++) {
                    if (park[i].charAt(initX) == 'X') {
                        y = initY;
                        break;
                    }
                    y = initY + move;
                }
            }
            // System.out.printf("%s initX: %d, initY: %d, x: %d, y: %d\n", dir, initX, initY, x, y);
        }
        int[] answer = {y, x};
        return answer;
    }
}