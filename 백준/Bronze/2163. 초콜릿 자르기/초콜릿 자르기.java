import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = 0;
        int m = 0;

        for(int i=0;st.hasMoreTokens();i++) {
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
        }
        //min(n,m)-1 + min(n,m)*(max(n,m)-1)
        int min = Math.min(n,m);
        int max = Math.max(n,m);
        sb.append(min-1+min*(max-1));
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception{
        new Main().solution();
    }
}
