s = input()

# 팰린드롬으로 만드려면 i번째(0 <= i <= len(s)-1)부터 끝까지 문자열을 뒤집은 문자열을 뒤에 붙여야함

for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(len(s) + i)
        break
