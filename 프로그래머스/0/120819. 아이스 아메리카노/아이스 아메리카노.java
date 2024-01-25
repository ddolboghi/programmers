class Solution {
    public int[] solution(int money) {
        int cnt = money / 5500;
        int[] answer = {cnt, money - (cnt * 5500)};//[잔 수, 잔돈]
        return answer;
    }
}