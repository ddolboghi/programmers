function solution(n, t, m, p) {
    var answer = '';
    let deci = 0;
    let total = '';
    let lastIdx = m*t-(m-p)-1;
    for (let i = 0; i < m*t; i++) {
        if (total.length > lastIdx) {
            break;
        }
        total += deci.toString(n).toUpperCase();
        deci++;
    }
    console.log(total);
    
    let idx = p-1;
    for (let str of total) {
        if (answer.length === t) break;
        answer += total.substr(idx, 1);
        idx += m;
    }
    return answer;
}