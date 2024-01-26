import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static List<List<int[]>> pickAll = new ArrayList<>();
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] firstLine = br.readLine().split(" ");
        n = Integer.parseInt(firstLine[0]);
        int m = Integer.parseInt(firstLine[1]);//뽑을 치킨집 개수
        List<int[]> homes = new ArrayList<>();
        List<int[]> chickens = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int pos = Integer.parseInt(st.nextToken());
                if (pos == 1) {
                    int[] home = {i, j};
                    homes.add(home);
                } else if (pos == 2) {
                    int[] chicken = {i, j};
                    chickens.add(chicken);
                }
            }
        }

        boolean[] visited = new boolean[chickens.size()];
        comb(chickens, visited, 0, m);
        int min  = (n-1)*2*n*n;
        for (List<int[]> picks : pickAll) {
            min = Math.min(min, calculateDistance(homes, picks, (n-1)*2));
        }
        System.out.println(min);
    }

    private static int calculateDistance(List<int[]> homes, List<int[]> picks, int maxChickenDistance) {
        int distance = 0;
        int min = maxChickenDistance;
        for (int[] h : homes) {
            for (int[] p : picks) {
                min = Math.min(min, (Math.abs(h[0] - p[0]) + Math.abs(h[1] - p[1])));
            }
            distance += min;
            min = maxChickenDistance;
        }
        return distance;
    }

    private static void comb(List<int[]> chickens, boolean[] visited, int start, int m) {
        if (m == 0) {
            List<int[]> picks = new ArrayList<>();
            for (int i = 0; i < chickens.size(); i++) {
                if (visited[i]) {
                    picks.add(chickens.get(i));
                }
            }
            pickAll.add(picks);
            return;
        }
        for (int i = start; i < chickens.size(); i++) {
            visited[i] = true;
            comb(chickens, visited, i+1, m-1);
            visited[i] = false;
        }
    }
}
