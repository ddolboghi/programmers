import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input1 = br.readLine().split(" ");
        int n = Integer.parseInt(input1[0]);
        int m = Integer.parseInt(input1[1]);
        int[][] lab = new int[n][m];
        List<int[]> zeros = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                lab[i][j] = Integer.parseInt(st.nextToken());
                if (lab[i][j] == 0) {
                    zeros.add(new int[] {i, j});
                }
            }
        }
        boolean[] visited = new boolean[zeros.size()];
        List<List<int[]>> pickeds = new ArrayList<>();
        pick(zeros, visited, 0, 3, pickeds);
        int safe = 0;
        for (List<int[]> picked : pickeds) {
            int[][] wallLab = buildWall(lab, picked);
            safe = Math.max(safe, countZero(wallLab));
        }
        //모든 경우의 수에서 구한 각각의 0 개수 중 가장 큰 값 출력
        System.out.println(safe);
    }

    private static int countZero(int[][] wallLab) {
        //bfs로 2를 퍼뜨리고 남은 0의 개수 세서 반환하는 메서드
        int[] dx = {0, 0, -1, 1};//상하좌우
        int[] dy = {-1, 1, 0, 0};//상하좌우
        int cnt = 0;
        boolean[][] visited = new boolean[wallLab.length][wallLab[0].length];

        for (int i = 0; i < wallLab.length; i++) {
            for (int j = 0; j < wallLab[0].length; j++) {
                if (wallLab[i][j] == 2 && !visited[i][j]) {
                    Queue<int[]> q = new LinkedList<>();
                    q.offer(new int[] {i, j});
                    visited[i][j] = true;
                    while (!q.isEmpty()) {
                        int[] v = q.poll();
                        for (int k = 0; k < 4; k++) {
                            int x = v[1] + dx[k];
                            int y = v[0] + dy[k];
                            if (0<=x && x<wallLab[0].length && 0<=y && y<wallLab.length && !visited[y][x] && wallLab[y][x] == 0) {
                                visited[y][x] = true;
                                wallLab[y][x] = 2;
                                q.offer(new int[] {y, x});
                            }
                        }
                    }
                }
            }
        }

        for (int[] row : wallLab) {
            for (int pos : row) {
                if (pos == 0) {
                    cnt += 1;
                }
            }
        }
        return cnt;
    }

    private static int[][] buildWall(int[][] lab, List<int[]> picked) {
        //0인 곳 3군데만 1로 바꾸는 경우의 수
        int[][] copy = new int[lab.length][lab[0].length];
        for (int i = 0; i < lab.length; i++) {
            System.arraycopy(lab[i], 0, copy[i], 0, copy[i].length);
        }
        for (int[] p : picked) {
            copy[p[0]][p[1]] = 1;
        }
        return copy;
    }

    private static void pick(List<int[]> zeros, boolean[] visited, int start, int r, List<List<int[]>> pickeds) {
        if (r == 0) {
            pickeds.add(pickedZeros(zeros, visited));
            return;
        }
        for (int i = start; i<zeros.size(); i++) {
            visited[i] = true;
            pick(zeros, visited, i+1, r-1, pickeds);
            visited[i] = false;
        }

    }

    private static List<int[]> pickedZeros(List<int[]> zeros, boolean[] visited) {
        List<int[]> picked = new ArrayList<>();
        for (int i = 0; i < zeros.size(); i++) {
            if (visited[i]) {
                picked.add(zeros.get(i));
            }
        }
        return picked;
    }
}
