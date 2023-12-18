import java.util.*;
class Solution {
    public int solution(String name) {
        //idx1 = 문자 위치
        //idx2 = idx1보다 크고 가장 가까운 A가 아닌 문자의 위치, 없다면 문자열 길이가 됨
        //L1 = idx1 - 0 = idx1
        //L2 = name.length() - idx2
        //최소 이동거리 = min(정역방향:L1*2 + L2, 역정방향:L2*2 + L1) = L1 + L2 + min(L1, L2)
        //문자열 처음부터 끝까지 돌며 각 위치에서 정방향, 정역방향, 역정방향 중 최솟값 찾기
        int answer = 0;
        int L2 = 0;
        int minMove = name.length()-1;
        
        for (int idx1=0; idx1 < name.length(); idx1++) {
            char now = name.charAt(idx1);
            //상하 이동 횟수
            answer += min('Z' - now + 1, now - 'A');
            
            int idx2 = idx1 + 1;
            while (idx2 < name.length()) {
                if (name.charAt(idx2) != 'A') {
                    break;
                }
                idx2++;
            }
            L2 = name.length() - idx2;
            minMove = min(minMove, idx1 + L2 + min(idx1, L2));
        }
        answer += minMove;
        return answer;
    }
    
    private int min(int a, int b) {
        return a > b ? b : a;
    }
}