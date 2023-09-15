class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        double length = arr.length;
        double sum = 0;
        for(double i : arr) {
            sum += i;
        }
        answer = sum/length;
        return answer;
    }
}