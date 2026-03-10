# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

# 입력이 하나씩 주어지면
# 그걸 배열에 받아서 최대값을 갱신하고
# 최대값과 인덱스 번호 출력

result =[]
maxNum = -1
idx = -1
for i in range(9):
     result.append(input())
     if maxNum < result[i]:
         maxNum = result[i]
         idx = i+1

if maxNum > 0 and idx > 0:
    print(maxNum)
    print(idx)



