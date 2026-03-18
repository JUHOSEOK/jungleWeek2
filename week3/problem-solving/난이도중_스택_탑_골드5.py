# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

# 오른쪽에서 왼쪽으로 감지하는 타워를 보면 스택에 쌓음?
# 끝에서부터 해야함

# 입력:
# 1. 탑의개수
# 2. 탑의 높이들
#
# 출력:
# 현재 탑에서 감지하는 탑의 인덱스번호

# 1. 입력받은 탑의 높이들을 리스트에 저장한다.
# 1.1 탑의 자리에 맞게 감지한 타워 저장할 리스트 초기화한다.
# 2. 뒤에서부터 하나씩 처음은 무조건 스택에 샇고 두번째 부터는 스텍이 있는거와 검사를한다.
# 2.1 만약 현재 값 스택에 있는거보다 크다면 스택을 없애고 현재값을 스택에 쌓고. (인덱스 번호를 변수값으로 해야하나 아니면 뒤에서부터 append하는게있나 [::-1] 이런것처럼)맨뒤에서부터 append한다.?
# 2.2 만약 작다면 스택을 위에 쌓고 다음 인덱스값을 비교한다.


N = int(input())
top_arr = list(map(int,input().split()))

stack = []
sense_top_arr = [0 for _ in range(N)]
length = len(top_arr)-1


for i in range(length,-1,-1):

    while stack and top_arr[stack[-1]] < top_arr[i]:
        target_idx = stack.pop()
        sense_top_arr[target_idx] = i + 1  # 현재 탑의 번호(1부터 시작) 기록

    stack.append(i)

print(*sense_top_arr)

# while 문을 사용해서 문제를 풀대 문제가 요구하는 사항에 맞게 구현이 힘들었ㅇ므
# 계쏙 스택의 위를 보고 현재와 비교해서 현재가 크다면 돌리는거잖아 그리고 stack이 잇을때만 계속 while문 돌리는거고


