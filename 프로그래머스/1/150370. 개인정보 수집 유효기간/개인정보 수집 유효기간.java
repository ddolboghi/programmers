import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> deleteList = new ArrayList<>();
        int nowYear = Integer.parseInt(today.substring(0, 4));
        int nowMonth = Integer.parseInt(today.substring(5, 7));
        int nowDay = Integer.parseInt(today.substring(8, 10));
        
        Map<String, Integer> termCases = new HashMap<>();
        for (String term : terms) {
            String[] termCase = term.split(" ");
            termCases.put(termCase[0], Integer.parseInt(termCase[1]));
        }
        
        for (int i=0;i<privacies.length;i++) {
            int year = Integer.parseInt(privacies[i].substring(0, 4));
            int month = Integer.parseInt(privacies[i].substring(5, 7));
            int day = Integer.parseInt(privacies[i].substring(8, 10));
            //day는 28일로 고정되있으므로 불변
            
            String term = privacies[i].substring(11);
            
            int sumMonth = month + termCases.get(term);
            year += sumMonth / 12;
            int newMonth = sumMonth % 12;
            day -= 1;
            if (day == 0) {
                newMonth -= 1;
                day = 28;
            }
            
            if (newMonth == 0) {
                year -= 1;
                newMonth = 12;
            }
            
            if (year < nowYear) {
                deleteList.add(i+1);
            } else if (year == nowYear) {
                if(newMonth < nowMonth) {
                    deleteList.add(i+1);
                } else if (newMonth == nowMonth) {
                    if (day < nowDay) {
                        deleteList.add(i+1);
                    }
                }
            }
        }
        Collections.sort(deleteList);
        int[] answer = deleteList.stream()
                .mapToInt(Integer::intValue)
                .toArray();
        
        return answer;
    }
    
}