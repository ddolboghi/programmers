import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i=1;i<=n;i*=10)
            answer += (n%(i*10)-n%i)/i;
        if(n == 1)
            return 1;
        return answer;
    }
}