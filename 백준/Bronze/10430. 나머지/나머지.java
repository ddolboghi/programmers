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

        int a = 0;
        int b = 0;
        int c = 0;

        for(int i=0;st.hasMoreTokens();i++) {
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
        }

        sb
                .append((a+b)%c).append('\n')
                .append(((a%c)+(b%c))%c).append('\n')
                .append((a*b)%c).append('\n')
                .append(((a%c)*(b%c))%c);
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception{
        new Main().solution();
    }
}
