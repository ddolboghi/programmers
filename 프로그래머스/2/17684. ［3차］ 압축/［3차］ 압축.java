import java.util.*;
class Solution {
    public int[] solution(String msg) {
        
        Map<String, Integer> dict = new HashMap<>();
        for (char c = 'A'; c <= 'Z'; c++) {
            dict.put(String.valueOf(c), Character.getNumericValue(c)-9);
        }
        List<Integer> list = new ArrayList<>();
        
        LZW(dict, list, msg);
        
        int[] answer = new int[list.size()];
        int idx = 0;
        for (int num : list) {
            answer[idx] = num;
            idx++;
        }
        System.out.println(msg.substring(1));
        return answer;
    }
    
    private void LZW(Map<String, Integer> dict, List<Integer> list, String w) {
        for (int i = 0; i < w.length(); i++) {
            String wc = w.substring(0, i+1); //한 글자씩 붙이기
            if (!dict.containsKey(wc)) {
                dict.put(wc, dict.size()+1); //사전에 없으면 추가
                list.add(dict.get(w.substring(0, i))); //직전 문자열은 사전에 있었으니 출력
                LZW(dict, list, w.substring(i)); //이전 문자열의 직후 문자부터 다시 시작 
                break; //사전에 없는게 나오면 멈춰야함
            } else {
                if (i+1 == w.length()) { //마지막 문자 출력
                    list.add(dict.get(w)); 
                }
            }
        }
    }
}