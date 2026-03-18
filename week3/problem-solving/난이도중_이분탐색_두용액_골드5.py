# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

# 입력:
# 1. 숫자개수
# 2. 숫자들
#
# 출력:
# 1. 두수를 연산햇을때 0 의 가장 가까운 두수
# 1. for 문으로 타겟으로 고를값을 정한다.
# 2. 타겟값과 가장 동떨어진값 ex) -2 == +2를 찾는다.
# 3. 없다면 가장 근처값을 찾아 min(함수로 저장한다.)

S = int(input())
arr = list(map(int, input().split()))
arr.sort()

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # 왜 범위가 1개일때는 생각하지 못했을까
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1

    return left

min_num = float('inf')

for i in range(S):
    value = int(arr[i])
    target = -value

    idx = binary_search(arr, target)
    # print("왼쪽",left,"오른쪽",right)

    # 배열에다가 다 넣어놓고 해시테이블에 넣어놓고 0 -1 0-1 0-1 0-1 같이 중복나오면은 0 -1 밖에 없을테니 양수만 뽑고
    # 만약에 그 뽑은 수가 2개 이상이 아니라면 arr + 뽑은수 즉 바로 옆에 수 를 가져와서 결과값으로 하기?
    #
    # 왼쪽자리번호 0 보다 커야하고 같은 자리(i) 와 같으면 안됨 그럴때 아니면 append하는식으로?

    # idx 주변의 3자리(왼쪽, 현재, 오른쪽)를 모두 후보에 넣고 검사
    candidates = [idx - 1, idx, idx + 1]

    for output in candidates:
            # 1번 조건: 배열 범위를 벗어나지 않는가? (낭떠러지 방지)
            # 2번 조건: 지금 내가 쥐고 있는 용액(i)이 아닌가? (나 자신 방지)

        if 0 <= output < S and output != i:
            current_sum = abs(arr[output] + value)

            if min_num > current_sum:
                min_num = current_sum
                ans1 = arr[output]
                ans2 = value

result_arr = [ans1,ans2]
result_arr.sort()
print(" ".join(map(str,result_arr)))









