import java.lang.Math.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        int half = (int) Math.sqrt(n);
        for(int i=1;i<=half;i++) {
            if(n%i == 0 ) {
                if(n/i != i) {
                    answer += i+(n/i);
                } else {
                    answer += i;
                }
            }
        }
        
        return answer;
    }
}