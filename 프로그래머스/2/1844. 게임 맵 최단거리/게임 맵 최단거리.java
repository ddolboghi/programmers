import java.util.*;
class Solution {
    static int n;
    static int m;
    static boolean[][] visited;
    public int solution(int[][] maps) {
        n = maps.length;
        m = maps[0].length;
        visited = new boolean[n][m];
        int[] start = {0, 0};
        
        bfs(start, maps);
        
        // for (int[] r: maps) {
        //     for (int c : r) {
        //         System.out.printf("%d ", c);
        //     }
        //     System.out.println();
        // }
        
        return maps[n-1][m-1] == 1 ? -1 : maps[n-1][m-1];
    }
    
    private static void bfs(int[] start, int[][] maps) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(start);
        
        int[] dx = {0, 0, -1, 1};
        int[] dy = {1, -1, 0, 0};

        while (!q.isEmpty()) {
            int[] v = q.poll();
            
            if (!visited[v[0]][v[1]]) {
                visited[v[0]][v[1]] = true;
                for (int i = 0; i < 4; i++) {
                    int x = v[1] + dx[i];
                    int y = v[0] + dy[i];
                    
                    if (0<=x && x<m && 0<=y && y<n && maps[y][x] == 1 && !visited[y][x]) {
                        maps[y][x] += maps[v[0]][v[1]]; //이전 위치의 값을 인접 위치에 더함
                        int[] adjP = {y, x};
                        q.offer(adjP);
                    }
                }
            }
        }
    }
}