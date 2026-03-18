# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

# A를 B번 곱한 수를 C로 나눈 나머지
# R = (A^B % C)
# A^B =  (A^B/2 * A^B/2)
#
# 입력: A B C 값
#
# 출력: A를 B번 곱한 수를 C로 나눈 나머지


def div(A,B,C):
    if B == 1:
        return A % C

    result = div(A, B//2, C)

    if B % 2 == 0:
        return (result * result) % C
    else:
        return ((result * result) * A) % C



arr = list(map(int,input().split()))

print(div(arr[0], arr[1], arr[2]))