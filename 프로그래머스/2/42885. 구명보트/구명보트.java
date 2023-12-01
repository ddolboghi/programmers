import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        //오름차순으로 정렬후 양끝 합 투포인터
        //양끝 합 > limit --> 큰값 위치-1
        //양끝 합 <= limit --> 둘다 구출되므로 다른 값이랑 비교할 필요 없고 양끝 위치 +-1
        Arrays.sort(people);
        int start = 0;
        int end = people.length-1;
        while (start <= end) {
            if (people[start] + people[end] > limit) {
                answer++;
                end--;
            } else {
                answer++;
                start++;
                end--;
            }
        }
        return answer;
    }
}