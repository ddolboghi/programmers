import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
        	String[] info = br.readLine().split(" ");
            int m = Integer.parseInt(info[0]);
            int n = Integer.parseInt(info[1]);
            int k = Integer.parseInt(info[2]);
        	int[][] bechus = new int[n][m];
        	
        	for (int i = 0 ; i < k ; i++) {
        		String[] pos = br.readLine().split(" ");
        		int x = Integer.parseInt(pos[0]);
        		int y = Integer.parseInt(pos[1]);
        		bechus[y][x] = 1;
        	}
        	int[][] visited = new int[n][m];
        	int cnt = 0;
        	for (int i = 0; i < n; i++) {
        		for (int j = 0; j < m; j++) {
        			if (bechus[i][j] == 1 && visited[i][j] == 0) {        				
        				int[] p = {i, j};
        				bfs(bechus, p, n, m, visited);
        				cnt++;
        			}
        		}
        	}
        	System.out.println(cnt);
        }
	}
	
	private static void bfs(int[][] bechus, int[] p, int n, int m, int[][] visited) {
		Queue<int[]> q = new LinkedList<>();
		q.offer(p);
		visited[p[0]][p[1]] = 1;
		int[] dx = {0, 0, -1, 1};
		int[] dy = {1, -1, 0, 0};
		
		while (!q.isEmpty()) {
			int[] pp = q.poll();
			int x = pp[1];
			int y = pp[0];
			for (int i = 0; i < 4; i++) {
				int xx = x + dx[i];
				int yy = y + dy[i];
				
				if ((0 <= xx && xx < m) && (0 <= yy && yy < n) && (bechus[yy][xx] == 1) && visited[yy][xx] == 0) {
					int[] ppp = {yy, xx};
					q.offer(ppp);
					visited[yy][xx] = 1;
				}
			}
		}
	}
}
