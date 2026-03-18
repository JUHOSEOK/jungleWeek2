# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
#
# 입력:
# 1. 한변의 길이 ex) 8 -> 8 * 8 격자배열
# 2. 각자리의 하얀색, 파란색 범위
#
# 출력:
# 1.

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0

def solve(x, y, N):
    global blue
    global white

    color = arr[x][y]  # 첫 번째 칸의 색을 기준으로 잡아요
    mid = N // 2
    for i in range(x, x + N):
        for j in range(y, y + N):

            if arr[i][j] != color:
                solve(x, y, N // 2)
                solve(x, y+mid, N // 2)
                solve(x+mid, y+mid, N // 2)
                solve(x+mid, y, N // 2)

                return

    if color == 0:
        white += 1
    else:
        blue += 1

solve(0,0,N)
print(white, blue, sep="\n")