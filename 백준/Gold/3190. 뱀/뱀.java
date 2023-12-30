import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        List<int[]> apples = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            String[] applePosInput = br.readLine().split(" ");
            int[] applePos = {Integer.parseInt(applePosInput[0]), Integer.parseInt(applePosInput[1])};
            apples.add(applePos);
        }
        int l = Integer.parseInt(br.readLine());
        Queue<String[]> changes = new LinkedList<>();
        for (int i = 0; i < l; i++) {
            String[] change = br.readLine().split(" ");
            changes.offer(change);
        }

        String dir = "E";
        List<int[]> snake = new ArrayList<>();
        int[] start = {1, 1};
        snake.add(start);
        int[] p = snake.get(0);
        int second = 0;

        while ((0<p[0] && p[0]<=n) && (0<p[1] && p[1]<=n)) {
            //매번 changes.poll()[0]과 second 비교 후
            //같으면 dir과 changes.poll()[1]을 changeDir함수로 보내고 dir 갱신
            if (!changes.isEmpty()) {
                String[] change = changes.peek();
                if (Integer.parseInt(change[0]) == second) {
                    dir = changeDir(dir, change[1]);
                    changes.remove();
                }
            }

            //dir에따라 이동할 p값(==newP) 계산
            p = snake.get(snake.size()-1);
            int[] newP = calculateP(p, dir);
            second++;
            //newP가 범위 내고, snake안에 없다면
            //해당 위치로 이동 add,
            //해당 위치에 사과가 없다면 add, remove(0)
            if (isMoving(newP, n, snake)) {
                snake.add(newP);
                boolean isApple = false;
                for (int[] apple : apples) {
                    if (Arrays.equals(apple, newP)) {
                        apples.remove(apple);
                        isApple = true;
                        break;
                    }
                }
                if (!isApple) {
                    snake.remove(0);
                }
            } else {
                break;
            }
        }
        System.out.println(second);
    }

    private static String changeDir(String dir, String changeInfo) {
        if (dir.equals("N") && changeInfo.equals("L")) {
            return "W";
        } else if (dir.equals("N") && changeInfo.equals("D")) {
            return "E";
        } else if (dir.equals("S") && changeInfo.equals("L") ) {
            return "E";
        } else if (dir.equals("S") && changeInfo.equals("D")) {
            return "W";
        } else if (dir.equals("E") && changeInfo.equals("L")) {
            return "N";
        } else if (dir.equals("E") && changeInfo.equals("D")) {
            return "S";
        } else if (dir.equals("W") && changeInfo.equals("L")) {
            return "S";
        } else {
            return "N";
        }
    }

    private static int[] calculateP(int[] p, String dir) {
        //dir: changeDir의 반환값
        int[] newP = Arrays.copyOf(p, p.length);
        if (dir.equals("N")) {
            newP[0] -= 1;
        } else if (dir.equals("S")) {
            newP[0] += 1;
        } else if (dir.equals("W")) {
            newP[1] -= 1;
        } else {
            newP[1] += 1;
        }
        return newP;
    }

    private static boolean isMoving(int[] newP, int n, List<int[]> snake) {
        if ((0<newP[0] && newP[0]<=n) && (0<newP[1] && newP[1]<=n)) {
            //이동할 위치에 뱀이 있다면 게임 종료
            for (int[] snakePos : snake) {
                if (Arrays.equals(snakePos, newP)) {
                    return false;
                }
            }
            return true;
        }
        //이동할 위치가 범위를 벗어나면 게임 종료
        return false;
    }
}
