def update_solution(current_x, current_y):
    global best_x, best_y, min_sum_xy, min_total_mass

    # x, y는 음이 아닌 정수여야 함
    if current_x < 0 or current_y < 0:
        return

    current_s_xy = current_x + current_y
    # 총 질량은 항상 a*current_x + b*current_y 로 계산
    current_t_mass = a * current_x + b * current_y

    if current_s_xy < min_sum_xy:  # 1순위: 추의 개수 최소화
        min_sum_xy = current_s_xy
        min_total_mass = current_t_mass
        best_x = current_x
        best_y = current_y
    elif current_s_xy == min_sum_xy:  # 2순위: 추의 개수가 같다면 총 질량 최소화
        if current_t_mass < min_total_mass:
            min_total_mass = current_t_mass
            best_x = current_x
            best_y = current_y


results_output = []
while True:
    a, b, d = map(int, input().split())
    if a == 0 and b == 0 and d == 0:
        break

    best_x = -1
    best_y = -1

    min_sum_xy = float("inf")
    min_total_mass = float("inf")

    # 경우 1: a*x + b*y = d
    # x는 0부터 d/a 까지 탐색
    if a > 0:
        for x_cand in range(d // a + 1):
            ax_val = a * x_cand
            if (d - ax_val) >= 0 and (d - ax_val) % b == 0:
                y_cand = (d - ax_val) // b
                update_solution(x_cand, y_cand)
    elif b > 0:  # a=0 이고 b>0 이면 b*y = d
        if d % b == 0:
            y_cand = d // b
            update_solution(0, y_cand)

    # 경우 2: a*x - b*y = d  (즉, a*x = d + b*y)
    # y는 0부터 a-1 까지 탐색 (이 범위에서 해가 존재하면 x+y가 최소인 해를 찾을 수 있음)
    # (d + b*y)가 a의 배수여야 함
    if a > 0:
        for y_cand in range(a):  # y_cand는 0부터 a-1까지
            by_val = b * y_cand
            if (d + by_val) >= 0 and (d + by_val) % a == 0:  # (d+by_val)은 항상 양수
                x_cand = (d + by_val) // a
                update_solution(x_cand, y_cand)

    # 경우 3: b*y - a*x = d  (즉, b*y = d + a*x)
    # x는 0부터 b-1 까지 탐색
    # (d + a*x)가 b의 배수여야 함
    if b > 0:
        for x_cand in range(b):  # x_cand는 0부터 b-1까지
            ax_val = a * x_cand
            if (d + ax_val) >= 0 and (d + ax_val) % b == 0:  # (d+ax_val)은 항상 양수
                y_cand = (d + ax_val) // b
                update_solution(x_cand, y_cand)

    results_output.append(f"{best_x} {best_y}")

for res in results_output:
    print(res)
