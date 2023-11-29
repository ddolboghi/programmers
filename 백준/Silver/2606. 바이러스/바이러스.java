import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int m = Integer.parseInt(br.readLine().trim());
        List<List<Integer>> graph = new ArrayList<>();
        for (int i=0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int j=0; j < m; j++) {
            String[] values = br.readLine().split(" ");
            int node1 = Integer.parseInt(values[0]);
            int node2 = Integer.parseInt(values[1]);

            graph.get(node1).add(node2);
            graph.get(node2).add(node1);
        }

        boolean[] visited = new boolean[n+1];
        Arrays.fill(visited, false);

        System.out.println(bfs(graph, visited));
    }

    private int bfs(List<List<Integer>> graph, boolean[] visited) {
        int count = 0;
        int start = 1;
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;

        while (!q.isEmpty()) {
            int v = q.poll();

            for (int node : graph.get(v)) {
                if (!visited[node]) {
                    visited[node] = true;
                    q.add(node);
                    count++;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}
