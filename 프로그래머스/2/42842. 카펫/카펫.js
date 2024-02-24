function solution(brown, yellow) {
    var answer = [];
    for (let col = 1; col <= yellow**0.5; col++) {
        let row = yellow / col;
        if ((row*2 + col*2 + 4) === brown) {
            answer.push(row+2);
            answer.push(col+2);
            break;
        }        
    }
    return answer;
}