def solution(picks, minerals):    
    # 1. 광물 5개씩 구간별로 곡괭이 개수만큼 담기
    # 2. 다이아, 철, 돌 개수가 많은 순서대로 내림차순 정렬
    # 3. 피로도 계산
    minerals = sorted([minerals[i:i+5] for i in range(0, len(minerals), 5)][:sum(picks)], key=lambda x: (x.count("diamond"), x.count("iron"), x.count("stone")), reverse=True)
    
    diaP, ironP, stoneP = picks
    
    diaStress = {"diamond": 1, "iron": 1, "stone": 1}
    ironStress = {"diamond": 5, 'iron': 1, "stone": 1}
    stoneStress = {"diamond": 25, "iron": 5, "stone": 1}
    
    answer = 0
    for interval in minerals:
        if diaP > 0:
            for m in interval:
                answer += diaStress[m]
            diaP -= 1
        
        elif ironP > 0:
            for m in interval:
                answer += ironStress[m]
            ironP -= 1
            
        elif stoneP > 0:
            for m in interval:
                answer += stoneStress[m]
            stoneP -= 1    
    
    return answer