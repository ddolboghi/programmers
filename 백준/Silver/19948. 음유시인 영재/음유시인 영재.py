content = input()
title = "".join([word[0].upper() for word in content.split()])
space_cnt = int(input())
keyboard_cnt = dict(zip("abcdefghijklmnopqrstuvwxyz", map(int, input().split())))
keyboard_cnt[" "] = space_cnt

# 대소문자 상관없이 keyboard_cnt에서 개수 차감
# 같은 문자나 빈칸이 연속하면 한 번만 차감
# 차감되기 전에 space_cnt나 keyboard_cnt의 value 중 하나라도 0이면 중단하고 -1 출력
# title과 content 따로 차감


def is_possible_write(string):
    continuous_str = string[0]
    for i in range(len(string)):
        if string[i] != continuous_str:
            cnt_key = continuous_str.lower()

            # 이전 문자의 남은 개수가 0 이하면 중단
            if keyboard_cnt[cnt_key] <= 0:
                return False
            # 연속한 문자나 빈칸은 continuous_str이 바뀌기 전에 1개 차감
            keyboard_cnt[cnt_key] -= 1
            # continuous_str에 현재 문자 할당
            continuous_str = string[i]

        elif string[i] == continuous_str and i == len(string) - 1:
            cnt_key = string[i].lower()
            if keyboard_cnt[cnt_key] <= 0:
                return False
            keyboard_cnt[cnt_key] -= 1

    return True


if is_possible_write(title) and is_possible_write(content):
    print(title)
else:
    print(-1)
