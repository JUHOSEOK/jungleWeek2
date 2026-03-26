# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707

# bfs로 탐색하는데 서로 연관된거 있으면은 while queue 끝날때 +1 해주기?

# bfs()
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, vertex, visited_queue):

    queue = deque([start])

    visited_queue[start] = 1
    while queue:

        popleft_node = queue.popleft()


        for neighbor in (graph[popleft_node]):
            if visited_queue[neighbor] == 0:
                queue.append(neighbor)
                visited_queue[neighbor] = visited_queue[popleft_node] * -1

            elif visited_queue[neighbor] == visited_queue[popleft_node]:
                return False

    return True


case = int(input())

for _ in range(case):

    vertex, edge = map(int,input().split())
    graph = {i : [] for i in range(1, vertex+1)}
    visited_queue = [0] * (vertex+1)
    is_ans = True

    for j in range(edge):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, vertex+1):
        if visited_queue[i] == 0:
            if not bfs(i,vertex, visited_queue):
                is_ans = False
                break

    graph = {}

    if is_ans:
        print("YES")
    else:
        print("NO")





