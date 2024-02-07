import java.util.*;
class Solution {
    public int[] solution(int n, long k) {
        int[] answer = new int[n];
        List<Integer> people = new ArrayList<>();
        long all = 1;
        for (int i = 1; i <= n; i++) {
            people.add(i);
            all *= i;
        }
        
        int idx = 0;
        k--;
        while (idx < n) {
            all /= n - idx;
                
            answer[idx++] = people.remove((int) (k / all));
            //다음 k
            k %= all;
        }
        
        return answer;
    }
}