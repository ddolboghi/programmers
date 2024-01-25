import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[][] gears = new int[4][8];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 4; i++) {
            String inputGear = br.readLine();
            for (int j = 0; j < 8; j++) {
                gears[i][j] = inputGear.charAt(j) - '0';
            }
        }

        StringTokenizer st;
        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int gearNum = Integer.parseInt(st.nextToken())-1;
            int dir = Integer.parseInt(st.nextToken());
            rotateAll(gearNum, dir);
        }

        int sum = 0;
        for (int i = 0; i < 4; i++) {
            sum += (int) (Math.pow(2, i) * gears[i][0]);
        }
        System.out.println(sum);
    }

    private static void rotateAll(int gearNum, int dir) {
        rotateR(gearNum+1, -dir);
        rotateL(gearNum-1, -dir);
        rotate(gearNum, dir);
    }

    private static void rotateR(int gearNum, int dir) {
        if (gearNum > 3 || gears[gearNum-1][2] == gears[gearNum][6]) return;
        rotateR(gearNum+1, -dir);
        rotate(gearNum, dir);
    }

    private static void rotateL(int gearNum, int dir) {
        if (gearNum < 0 || gears[gearNum][2] == gears[gearNum+1][6]) return;
        rotateL(gearNum-1, -dir);
        rotate(gearNum, dir);
    }
    
    private static void rotate(int gearNum, int dir) {
        if (dir == 1) {
            int tmp = gears[gearNum][7];
            for (int i = 7; i > 0; i--) {
                gears[gearNum][i] = gears[gearNum][(i+7)%8];
            }
            gears[gearNum][0] = tmp;
        } else {
            int tmp = gears[gearNum][0];
            for (int i = 0; i < 7; i++) {
                gears[gearNum][i] = gears[gearNum][(i+1)%8];
            }
            gears[gearNum][7] = tmp;
        }
    }

}
