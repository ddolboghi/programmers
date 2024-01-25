class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];//[짝, 홀]
        for (int n : num_list) {
            if (n % 2 == 0) {
                answer[0] += 1;
            } else {
                answer[1] += 1;
            }
        }
        return answer;
    }
}