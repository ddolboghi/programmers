import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        List<List<Integer>> dates = new ArrayList<>();
        for (int i=0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            List<Integer> date = List.of(
                    Integer.parseInt(input[0]) * 100 + Integer.parseInt(input[1]),
                    Integer.parseInt(input[2]) * 100 + Integer.parseInt(input[3]));
            dates.add(date);
        }
        dates.sort(Comparator.comparing((List<Integer> list) -> list.get(0)));


        int end = 301; // 마지막 꽃의 지는 날짜
        int cnt = 0;
        while (!dates.isEmpty()) {
            if (dates.get(0).get(0) > end || end > 1130) { // 심을 꽃이 없거나(초기상태) 마지막 꽃의 지는 날짜가 지금 꽃의 피는 날짜보다 크거나 1130보다 크면 멈춤
                break;
            }

            int subEnd = 0;
            while (!dates.isEmpty()) {
                if (dates.get(0).get(0) <= end) { // 피는 날짜가 마지막 꽃의 지는 날짜보다 작거나 같으면 가장 큰 지는 날짜 구함
                    subEnd = Math.max(dates.get(0).get(1), subEnd);
                    dates.remove(0);
                } else { // 피는 날짜가 마지막 꽃의 지는 날짜보다 크면 멈춤
                    break;
                }
            }

            end = subEnd; // 가장 큰 지는 날짜가 마지막 꽃의 지는 날짜가 되거나 꽂이 필수 없는 기간이 생기면 0이됨
            cnt++;
        }

        if (end < 1201) {
            System.out.println(0);
        } else {
            System.out.println(cnt);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}
