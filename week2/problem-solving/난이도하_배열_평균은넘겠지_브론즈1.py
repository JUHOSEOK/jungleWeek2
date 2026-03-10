# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
#
# 입력:
# - 테스트 케이스 개수
# - 테스트케이스 리스트
#
# 출력:
# - 평균을 넘는 학생들의 비율
#
# 1. 테스트케이스 갯수 입력받음
# 2. 테스트케이스 갯수만큼 반복해 리스트에 입력받은 리스트를 추가함
# 3. 학생들의 수 만큼 접근하고 수를 더해 평균을 구함
# 4. 평균보다 높은 사람의수를 구하고 수 전체수 / 사람수 를 하여 평균을 넘는 학생들의 비율을 구하고 프린트함

# [ [50 50 70 80 100], [100 95 90 80 70 60 50], [70 90 80], [70 90 81], [100 99 98 97 96 95 94 93 91] ]

testNum = int(input())
testCase = []

# 평균을 넘는 학생 비율 구하는  함수
def average(studentLen):
    sum = 0
    # lenth = len(studentLen)
    lenth = int(studentLen[0])
    goodStu = 0

    for j in range(1, lenth+1):
        sum += int(studentLen[j])

    average = sum / lenth


    for k in range(1, lenth+1):
        if average < int(studentLen[k]):
            goodStu += 1

    return goodStu / lenth * 100


# 입출력
for i in range(testNum):
    testCase.append(input().split())

for i in range(testNum):

    # result = "{:.3f}".format(average(testCase[i]))
    # print(result)
    print(f"{average(testCase[i]):.3f}%")

















