import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        String[] inputWays = br.readLine().split(" ");
        String[] costs = br.readLine().split(" ");

        int remainWay = 0;
        for (String inputWay : inputWays) {
            remainWay += Integer.parseInt(inputWay);
        }

        String[] ways = Arrays.copyOf(inputWays, n);
        ways[n-1] = "0";
        
        int min = Integer.parseInt(costs[0]);
        int total = min * remainWay;
        for (int i = 0; i < n; i++) {
            int nowCost = Integer.parseInt(costs[i]);
            if (nowCost < min) {
                total = total - min*remainWay + nowCost*remainWay;
                min = nowCost;
            }
            remainWay -= Integer.parseInt(ways[i]);
        }

        System.out.println(total);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}
