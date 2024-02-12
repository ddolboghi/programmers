import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        //K보다 작은 원소들만 추출해 우선순위 큐에 넣음(최소 힙)
        //K보다 크거나 같은 원소 하나만 마지막으로 넣음
        PriorityQueue<Integer> scovs = new PriorityQueue<>();
        PriorityQueue<Integer> unders = new PriorityQueue<>();
        for (int s : scoville) {
            scovs.offer(s);
            if (s < K) {
                unders.offer(scovs.poll());
            }
        }
        if (scovs.size() > 0) {
            unders.offer(scovs.poll());
        }
        
        
        //위의 우선순위 큐는 가장 작은 원소부터 꺼내짐
        //2개 꺼내서 scov 계산하고 다시 넣음
        int answer = 0;
        while (unders.size() > 1 && unders.peek() < K) {            
            int u1 = unders.poll();
            int u2 = unders.poll();
            unders.offer(u1 + u2*2);
            answer++;
        }
        if (unders.size() > 0 && unders.peek() < K) {
            return -1;
        }
        
        System.out.println(unders);
        return answer;
    }
}